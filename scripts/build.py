"""Build offline reader from Markdown; Python stdlib only."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def build():
 pages=[]
 for base in ['wiki','workflow','reports','evidence','labs']:
  for p in sorted((ROOT/base).rglob('*.md')):
   text=p.read_text(encoding='utf-8'); title=next((s[2:] for s in text.splitlines() if s.startswith('# ')),p.stem)
   pages.append({'path':p.relative_to(ROOT).as_posix(),'title':title,'body':text})
 for name in ['README.md','AGENTS.md','SKILL.md','PRD.md','DESIGN.md']:
  p=ROOT/name;text=p.read_text(encoding='utf-8');pages.append({'path':name,'title':name.replace('.md',''),'body':text})
 catalog=json.loads((ROOT/'sources/catalog.json').read_text(encoding='utf-8'))
 data={'version':'course-wiki-v2','date':'2026-11-22','ingested':sum(x['status'] in ['ingested','pilot_ingested'] for x in catalog),'total':len(catalog),'pages':pages}
 serial=json.dumps(data,ensure_ascii=False)
 (ROOT/'site-data.json').write_text(serial+'\n',encoding='utf-8')
 template=(ROOT/'assets/template.html').read_text(encoding='utf-8')
 (ROOT/'index.html').write_text(template.replace('__WIKI_DATA__',serial.replace('<','\\u003c')),encoding='utf-8')
 print(f'Built {len(pages)} Markdown pages into index.html; content is embedded for file:// use.')
if __name__=='__main__': build()
