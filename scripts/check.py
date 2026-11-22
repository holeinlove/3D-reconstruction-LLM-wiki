"""Check declared invariants; does not replace source/semantic review."""
from pathlib import Path
import json,re,math
ROOT=Path(__file__).resolve().parents[1]
def run():
 errors=[]; results=[]
 def check(name,ok,detail):
  results.append({'check':name,'passed':bool(ok),'detail':detail})
  if not ok: errors.append(name)
 catalog=json.loads((ROOT/'sources/catalog.json').read_text(encoding='utf-8'))
 counts={x['id']:x['slides'] for x in catalog}
 coverage=json.loads((ROOT/'sources/coverage.json').read_text(encoding='utf-8'))
 check('S02 slide coverage',sorted(x['slide'] for x in coverage)==list(range(1,45)),f'{len(coverage)} entries; 44 actual slides')
 check('coverage targets',all((ROOT/x['target']).is_file() for x in coverage),'Every disposition points to a real page')
 check('phase boundary',sum(x['status']=='pilot_ingested' for x in catalog)==1,'Only S02 ingested; six pending')
 check('source fingerprint',bool(re.fullmatch('[0-9a-f]{64}',catalog[1].get('sha256',''))),'SHA-256 recorded for S02; original PPT not tracked')
 badlinks=[];badrefs=[];refcount=0;linkcount=0
 for p in ROOT.rglob('*.md'):
  if 'vendor' in p.parts: continue
  text=p.read_text(encoding='utf-8')
  for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
   if re.match(r'^(https?://|mailto:|#)',dest):continue
   linkcount+=1
   target=dest.split('#')[0]
   if target and not (p.parent/target).resolve().is_file():badlinks.append(str(p.relative_to(ROOT))+':'+dest)
  for sid,span in re.findall(r'\b(S\d{2})\s+p{1,2}\.([0-9,–—\-]+)',text):
   refcount+=1
   if sid not in counts or any(int(n)<1 or int(n)>counts.get(sid,0) for n in re.findall(r'\d+',span)):badrefs.append(sid+':'+span)
  if p.parent.name in ['concepts','cases']:
   if not re.search(r'S02\s+p{1,2}\.',text):badrefs.append(p.name+': missing precise source')
 check('Markdown links',not badlinks,{'checked':linkcount,'broken':badlinks})
 check('slide references',not badrefs,{'checked':refcount,'invalid':badrefs,'limit':'Range/identity check, not claim fidelity'})
 xp,yp=4.3*.005,1.3*.005;cx,cy=2048+4.3,1500-1.3
 check('textbook principal point',all(math.isclose(a,b,abs_tol=1e-10) for a,b in zip([xp,yp,cx,cy],[.0215,.0065,2052.3,1498.7])),{'PM_mm':[xp,yp],'CV_pixel':[cx,cy]})
 check('coordinate round trip',math.isclose((cx-2048)*.005,xp,abs_tol=1e-12) and math.isclose(-(cy-1500)*.005,yp,abs_tol=1e-12),'Forward and backward axes/units agree')
 residuals=[(.3,.4),(0,.5),(-.3,-.4),(0,-.5)]
 rmse=math.sqrt(sum(u*u+v*v for u,v in residuals)/len(residuals))
 check('self-created RMSE example',math.isclose(rmse,.5),{'value_pixel':rmse,'definition':'sqrt(sum du²+dv² / N); not a measured result'})
 check('self-created focal example',math.isclose(20/.005,4000),'20 mm / 0.005 mm/pixel = 4000 pixel')
 # A synthetic invertible correction c(d)=0.01d: validate sign after algebraic rearrangement.
 u=1.01;d=u
 for _ in range(8):d=u-.01*d
 check('inverse sign synthetic example',math.isclose(d,1,abs_tol=1e-12),'Known c(d)=0.01d; d=u-c(d). Does not validate textbook unknown coefficients.')
 for n in ['README.md','AGENTS.md','SKILL.md','PRD.md','DESIGN.md']:
  check('root document '+n,(ROOT/n).is_file(),n)
 asset_missing=[]
 for p in [ROOT/'index.html',ROOT/'assets/template.html']:
  if p.is_file():
   for rel in re.findall(r'(?:src|href)="([^"#]+)"',p.read_text(encoding='utf-8')):
    if not re.match(r'^(https?:|mailto:)',rel) and not (ROOT/rel).is_file():asset_missing.append(rel)
 css=(ROOT/'vendor/katex/katex.min.css').read_text(encoding='utf-8')
 for rel in re.findall(r'url\(([^)]+)\)',css):
  if not (ROOT/'vendor/katex'/rel).is_file():asset_missing.append(rel)
 check('offline asset files',not asset_missing,{'missing':asset_missing,'limit':'Presence check; file:// not separately browser-tested'})
 report={'date':'2026-11-22','timezone':'Asia/Taipei','passed':not errors,'checks':results,'limitations':['Not an independent AI review','Not a real camera calibration','Does not validate external network links or every mathematical claim']}
 (ROOT/'reports/checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))
 return not errors
if __name__=='__main__':raise SystemExit(0 if run() else 1)
