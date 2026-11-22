from pathlib import Path
import json,html

def render(D,output):
 sections=[]
 for i,s in enumerate(D['slides'],1):
  refs=''.join(f'<a href="../wiki.html#p={html.escape(r["path"],quote=True)}" target="_blank" rel="noopener">{html.escape(r["label"])}</a>' for r in s['refs'])
  lab=f'<div class="demo" data-module="{s["lab"]}"><h1 hidden>互動模組</h1></div>' if s['lab'] else ''
  note=f'<details class="notes"><summary>講解提示／答案</summary><p>{html.escape(s["note"])}</p></details>' if s['note'] else ''
  sections.append(f'<section class="slide" id="s{i}" aria-labelledby="title-{i}" data-index="{i}"><p class="eyebrow">影像感測與 3D 重建 / {"製作與反思" if s["kind"]=="process" else "概念與實作"}</p><h2 id="title-{i}">{html.escape(s["title"])}</h2><div class="body">{s["body"]}{lab}{note}</div><footer><span>{i:02d} / {len(D["slides"]):02d}</span><details class="source-notes"><summary>來源與延伸</summary><div class="refs">{refs}</div></details></footer></section>')
 options=''.join(f'<option value="{i}">{i:02d} · {html.escape(s["title"])}</option>' for i,s in enumerate(D['slides'],1))
 page='''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>兩張照片，如何變成 3D？｜互動教學簡報</title><link rel="stylesheet" href="../vendor/katex/katex.min.css"><link rel="stylesheet" href="../assets/labs.css"><link rel="stylesheet" href="slides.css"></head><body><a class="skip" href="#deck">跳至簡報</a><header class="toolbar"><a class="brand" href="../">3D 重建・學習筆記</a><details class="tools"><summary>選單</summary><div class="tools-panel"><label for="jump">跳至投影片</label><select id="jump" aria-label="選擇投影片">OPTIONS</select><button id="mode" aria-pressed="false">閱讀全部</button><button id="print">列印／PDF</button><a href="../wiki.html">回到 Wiki</a></div></details></header><main id="deck" tabindex="-1">SECTIONS</main><nav class="controls" aria-label="投影片控制"><button id="prev" aria-label="上一頁">‹</button><div id="dots" class="dots" aria-label="快速選頁"></div><output id="progress" aria-live="polite"></output><button id="next" aria-label="下一頁">›</button></nav><p class="keyboard">方向鍵換頁（操作滑桿時除外）· Home / End · 手機可捲動閱讀</p><noscript><p>JavaScript 已關閉：仍可閱讀全部投影片，互動示範需啟用 JavaScript。</p></noscript><script src="../vendor/katex/katex.min.js"></script><script src="../assets/lab-math.js"></script><script src="../assets/labs.js"></script><script src="slides.js"></script></body></html>'''.replace('OPTIONS',options).replace('SECTIONS','\n'.join(sections))
 page=page.replace('兩張照片，如何變成 3D？｜互動教學簡報',html.escape(D['title'])+'｜互動教學簡報').replace('href="../">3D 重建・學習筆記','href="index.html">← 七章課程')
 Path(output).write_text(page,encoding='utf-8')
 print('Built',output,len(D['slides']),'slides')

render(json.loads(Path('slides/deck.json').read_text(encoding='utf-8')),'slides/overview.html')
chapters=[]
for p in sorted(Path('slides/chapters').glob('*.json')):
 d=json.loads(p.read_text(encoding='utf-8'));chapters.append(d);render(d,f'slides/chapter-{d["chapter"]:02d}.html')
cards=[]
for d in chapters:
 n=d['chapter'];cards.append(f'''<a class="chapter-card" href="chapter-{n:02d}.html"><span class="chapter-number">第 {n:02d} 章</span><h2>{html.escape(d['title'])}</h2><p>{html.escape(d['description'])}</p><div class="card-meta"><span>{len(d['slides'])} 頁簡報</span><span>互動學習</span></div><strong>開始學習 →</strong></a>''')
landing='''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>影像感測與 3D 場景重建｜七章課程</title><link rel="stylesheet" href="catalog.css"></head><body><main><header><p class="brand">3D 重建・學習筆記</p><h1>選一章，<br>開始理解 3D 重建。</h1><p class="intro">從影像感測到立體點雲，依照課堂的七個章節學習。<br>點選章節，即可翻頁閱讀與操作示範。</p><div class="camera" aria-hidden="true"><span>◉</span><small>IMAGE → 3D</small></div></header><section aria-label="七章教學簡報" class="chapter-grid">CARDS</section><footer><span>以課堂 Wiki 為知識來源 · 保留推導、案例與來源頁碼</span><nav><a href="overview.html">課程總覽與作業流程</a><a href="../wiki.html">完整 Wiki</a></nav></footer></main></body></html>'''.replace('CARDS','\n'.join(cards))
Path('slides/index.html').write_text(landing,encoding='utf-8')
print('Built seven-chapter landing')

root_landing=landing.replace('href="catalog.css"','href="slides/catalog.css"').replace('href="chapter-','href="slides/chapter-').replace('href="overview.html"','href="slides/overview.html"').replace('href="../wiki.html"','href="wiki.html"')
root_landing=root_landing.replace('</body>','<script>if(location.hash.startsWith("#p="))location.replace("wiki.html"+location.hash);</script></body>')
Path('index.html').write_text(root_landing,encoding='utf-8')
print('Built root course landing; Wiki reader at wiki.html')
