"""Generate conservative WebP derivatives; never rewrite source assets."""
from pathlib import Path
from PIL import Image,features
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/optimized'
HTML=ROOT/'index.html'

def build():
 OUT.mkdir(parents=True,exist_ok=True)
 text=HTML.read_text(encoding='utf-8')
 sources=sorted(set(re.findall(r'assets/([\w-]+)\.webp',text)) | set(re.findall(r'assets/optimized/([\w-]+)-\d+\.webp',text)))
 records=[]
 for name in sources:
  src=ROOT/'assets'/f'{name}.webp'
  with Image.open(src) as im:
   im.load()
   widths=sorted(set([min(im.width,w) for w in (320,640,960,1280,im.width)]))
   for w in widths:
    size=(w,round(im.height*w/im.width))
    resized=im.resize(size,Image.Resampling.LANCZOS) if size!=im.size else im.copy()
    dest=OUT/f'{name}-{w}.webp'
    resized.save(dest,'WEBP',quality=90,method=6)
    with Image.open(dest) as decoded:
     assert decoded.size==size
    records.append({'source':f'assets/{name}.webp','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'source_bytes':src.stat().st_size,'path':dest.relative_to(ROOT).as_posix(),'width':w,'height':size[1],'bytes':dest.stat().st_size})
 (OUT/'manifest.json').write_text(json.dumps({'pillow':__import__('PIL').__version__,'libwebp':features.version('webp'),'quality':90,'method':6,'images':records},indent=2)+'\n',encoding='utf-8')
 print(f'Generated {len(records)} derivatives from {len(sources)} preserved sources')
if __name__=='__main__':build()
