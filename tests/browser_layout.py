"""Regression: mobile Blend CTA containment and right-aligned menu."""
from pathlib import Path
import threading,http.server,functools
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome')
 for width in (320,360,375,390,414,520,768,900,901,1280):
  page=b.new_page(viewport={'width':width,'height':900},reduced_motion='reduce')
  page.goto(f'http://127.0.0.1:{server.server_port}/');page.wait_for_timeout(150)
  card=page.locator('.prod-grid.single .product');quote=card.locator('.inquiry-button').last
  quote.scroll_into_view_if_needed();page.wait_for_timeout(100)
  cb=card.bounding_box();qb=quote.bounding_box()
  assert cb and qb
  assert qb['y']+qb['height']<=cb['y']+cb['height']-27.5,(width,'clipped quote',cb,qb)
  if width<=980:
   burger=page.locator('#burger');bb=burger.bounding_box();co=page.locator('.nav .container').bounding_box()
   assert bb and co
   assert abs(bb['x']+bb['width']-co['x']-co['width'])<1,(width,'burger not right aligned')
   assert page.locator('#menu').evaluate('(e)=>e.inert')
   burger.click();assert burger.get_attribute('aria-expanded')=='true'
   assert not page.locator('#menu').evaluate('(e)=>e.inert')
   page.locator('#menu a').first.focus();page.keyboard.press('Escape')
   assert burger.get_attribute('aria-expanded')=='false'
   assert burger.evaluate('(e)=>document.activeElement===e')
   assert page.locator('#menu').evaluate('(e)=>e.inert')
  else:assert not page.locator('#burger').is_visible()
  print('PASS layout/menu',width);page.close()
 b.close()
server.shutdown()
