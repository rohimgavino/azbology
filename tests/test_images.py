import unittest,re,json,hashlib
from pathlib import Path
from PIL import Image
from PIL import ImageChops,ImageStat
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
class Images(unittest.TestCase):
 def test_derivatives_preserve_sources_dimensions_and_quality(self):
  manifest=json.loads((ROOT/'assets/optimized/manifest.json').read_text())
  for v in manifest['images']:
   src=ROOT/v['source'];dest=ROOT/v['path']
   self.assertEqual(hashlib.sha256(src.read_bytes()).hexdigest(),v['source_sha256'])
   with Image.open(src) as source,Image.open(dest) as decoded:
    self.assertEqual(decoded.size,(v['width'],v['height']))
    self.assertLessEqual(decoded.width,source.width)
    self.assertAlmostEqual(decoded.height,source.height*decoded.width/source.width,delta=.51)
    reference=source.convert('RGBA').resize(decoded.size,Image.Resampling.LANCZOS)
    reference=Image.alpha_composite(Image.new('RGBA',decoded.size,'white'),reference).convert('RGB')
    display=Image.alpha_composite(Image.new('RGBA',decoded.size,'white'),decoded.convert('RGBA')).convert('RGB')
    error=ImageStat.Stat(ImageChops.difference(reference,display)).rms
    self.assertLess(max(error),12, v['path'])
    self.assertLess(dest.stat().st_size,src.stat().st_size,v['path'])
 def test_no_catalogue_downloads(self):
  soup=BeautifulSoup((ROOT/'index.html').read_text(encoding='utf-8'),'html.parser')
  self.assertFalse(soup.select('a[download],a[href$=".pdf"]'))
 def test_responsive_photos_replace_eager_backgrounds(self):
  soup=BeautifulSoup((ROOT/'index.html').read_text(encoding='utf-8'),'html.parser')
  photos=soup.select('.ph.has-img img')
  self.assertEqual(len(photos),38)
  self.assertFalse(soup.select('[style*="background-image:url"]'))
  for im in photos:
   self.assertTrue(im.get('srcset'));self.assertTrue(im.get('sizes'))
   self.assertGreater(int(str(im['width'])),0);self.assertGreater(int(str(im['height'])),0)
   self.assertEqual(im['loading'],'eager' if im.find_parent(id='home') else 'lazy')
if __name__=='__main__':unittest.main()
