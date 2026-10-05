"""Actual Chromium checks at required widths, JS on/off; local only."""
from pathlib import Path
import json,re,threading,http.server,functools,hashlib,subprocess,os
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
SCRATCH=Path(os.environ.get('AZBO_REPORT_DIR',str(Path.home()/'AppData/Local/hermes/cache/scratch/azbo-image-audit')))
SCRATCH.mkdir(parents=True,exist_ok=True)
BASELINE=subprocess.check_output(['git','show','6e15209:index.html'],cwd=ROOT)
geometry=[]
class Handler(http.server.SimpleHTTPRequestHandler):
 def log_message(self,format,*args):pass
 def do_GET(self):
  if self.path=='/baseline.html':
   data=BASELINE;self.send_response(200);self.send_header('Content-Type','text/html');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
  else:super().do_GET()
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome')
 for width in (375,768,1280):
  for js_enabled in (True,False):
   for baseline in (True,False):
    ctx=b.new_context(viewport={'width':width,'height':900},java_script_enabled=js_enabled,device_scale_factor=1,reduced_motion='reduce')
    page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(f'http://127.0.0.1:{server.server_port}/'+('baseline.html' if baseline else 'index.html'));page.wait_for_timeout(700)
    initial=page.evaluate("performance.getEntriesByType('resource').filter(x=>x.name.includes('/assets/')&&x.responseEnd).map(x=>({url:x.name,bytes:x.encodedBodySize}))")
    if baseline:
     geometry=page.locator('.ph.has-img').evaluate_all('(es)=>es.map(e=>({w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height}))')
    for el in page.locator('.ph.has-img').all():el.scroll_into_view_if_needed();page.wait_for_timeout(80)
    for el in page.locator('img').all():
     el.scroll_into_view_if_needed()
     page.wait_for_function('(e)=>e.complete && e.naturalWidth>0',arg=el.element_handle(),timeout=15000)
    page.wait_for_timeout(500)
    images=page.locator('img').evaluate_all('(es)=>es.map(e=>({src:e.currentSrc,ok:e.complete&&e.naturalWidth>0,w:e.naturalWidth,h:e.naturalHeight}))')
    assert all(i['ok'] for i in images),images
    assert not errors,errors
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),width
    assert not page.locator('a[download],a[href$=".pdf"]').count()
    if not baseline:
     current=page.locator('.ph.has-img').evaluate_all('(es)=>es.map(e=>({w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height}))')
     assert current==geometry,(width,current,geometry)
     assert len(images)==44,len(images)
    resources=page.evaluate("performance.getEntriesByType('resource').filter(x=>x.name.includes('/assets/')&&x.responseEnd).map(x=>({url:x.name,bytes:x.encodedBodySize}))")
    record={'width':width,'javascript':js_enabled,'baseline':baseline,'initial_image_body_bytes':sum(i['bytes'] for i in initial),'all_image_body_bytes':sum(i['bytes'] for i in resources),'loaded_images':len(images),'errors':errors,'resources':resources}
    results.append(record);print({k:v for k,v in record.items() if k!='resources'})
    if not baseline and js_enabled:page.screenshot(path=str(SCRATCH/f'optimized-{width}.png'),full_page=True)
    ctx.close()
 b.close()
server.shutdown()
(SCRATCH/'browser-results.json').write_text(json.dumps(results,indent=2))
print('PASS: all photos decode, wrapper geometry preserved, no overflow/download links/JS errors in 12 runs')
