from pathlib import Path
import json,html
D=json.loads(Path('slides/deck.json').read_text(encoding='utf-8'))
sections=[]
for i,s in enumerate(D['slides'],1):
 refs=''.join(f'<a href="../#p={html.escape(r["path"],quote=True)}" target="_blank" rel="noopener">{html.escape(r["label"])}</a>' for r in s['refs'])
 lab=f'<div class="demo" data-module="{s["lab"]}"><h1 hidden>互動模組</h1></div>' if s['lab'] else ''
 note=f'<details class="notes"><summary>講解提示／答案</summary><p>{html.escape(s["note"])}</p></details>' if s['note'] else ''
 sections.append(f'<section class="slide" id="s{i}" aria-labelledby="title-{i}" data-index="{i}"><p class="eyebrow">影像感測與 3D 重建 / {"製作與反思" if s["kind"]=="process" else "概念與實作"}</p><h2 id="title-{i}">{html.escape(s["title"])}</h2><div class="body">{s["body"]}{lab}{note}</div><footer><span>{i:02d} / {len(D["slides"]):02d}</span><div class="refs">{refs}</div></footer></section>')
options=''.join(f'<option value="{i}">{i:02d} · {html.escape(s["title"])}</option>' for i,s in enumerate(D['slides'],1))
page='''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>兩張照片，如何變成 3D？｜互動教學簡報</title><link rel="stylesheet" href="../vendor/katex/katex.min.css"><link rel="stylesheet" href="../assets/labs.css"><link rel="stylesheet" href="slides.css"></head><body><a class="skip" href="#deck">跳至簡報</a><header class="toolbar"><a href="../">← Wiki</a><label for="jump">章節</label><select id="jump" aria-label="選擇投影片">OPTIONS</select><button id="mode" aria-pressed="false">閱讀全部</button><button id="print">列印／PDF</button></header><main id="deck" tabindex="-1">SECTIONS</main><nav class="controls" aria-label="投影片控制"><button id="prev" aria-label="上一頁">← 上一頁</button><output id="progress" aria-live="polite"></output><button id="next" aria-label="下一頁">下一頁 →</button></nav><p class="keyboard">方向鍵換頁（操作滑桿時除外）· Home / End · 手機可捲動閱讀</p><noscript><p>JavaScript 已關閉：仍可閱讀全部投影片，互動示範需啟用 JavaScript。</p></noscript><script src="../vendor/katex/katex.min.js"></script><script src="../assets/lab-math.js"></script><script src="../assets/labs.js"></script><script src="slides.js"></script></body></html>'''.replace('OPTIONS',options).replace('SECTIONS','\n'.join(sections))
Path('slides/index.html').write_text(page,encoding='utf-8')
print('Built',len(sections),'slides')
