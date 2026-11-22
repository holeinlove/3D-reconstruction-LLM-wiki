/* Content stays in Markdown. All assets are local; no runtime network calls. */
(()=>{'use strict';
const data=JSON.parse(document.getElementById('wiki-data').textContent),pages=new Map(data.pages.map(p=>[p.path,p]));
const md=window.markdownit({html:false,linkify:true,typographer:false});
const search=document.getElementById('search'),nav=document.getElementById('nav');let current='wiki/index.md';
function escape(s){return s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function group(p){if(p.path.startsWith('labs/'))return '互動學習';if(p.path.startsWith('wiki/chapters'))return '章節導覽';if(p.path.startsWith('wiki/concepts'))return '概念與推導';if(p.path.startsWith('wiki/cases'))return '應用案例';if(p.path.startsWith('evidence/'))return '證據卡';if(!p.path.includes('/'))return '專案文件';return '來源與執行紀錄';}
function drawNav(){const q=search.value.trim().toLocaleLowerCase();let found=data.pages.filter(p=>!q||(p.title+' '+p.body).toLocaleLowerCase().includes(q));
 const order=['互動學習','章節導覽','概念與推導','應用案例','來源與執行紀錄','證據卡','專案文件'];nav.innerHTML='';
 if(!q){const a=document.createElement('a');a.className='nav-link';a.href='#p=wiki/index.md';a.textContent='Wiki 首頁';a.setAttribute('aria-current',current==='wiki/index.md'?'page':'false');nav.append(a);}
 for(const g of order){const subset=found.filter(p=>group(p)===g);if(!subset.length)continue;const label=document.createElement('div');label.className='nav-heading';label.textContent=g;nav.append(label);
 for(const p of subset){if(p.path==='wiki/index.md'&&!q)continue;const a=document.createElement('a');a.className='nav-link';a.href='#p='+encodeURIComponent(p.path);a.textContent=p.title;a.setAttribute('aria-current',p.path===current?'page':'false');nav.append(a);}}
 document.getElementById('search-status').textContent=q?`${found.length} 個符合頁面`:'';if(!found.length)nav.innerHTML='<p class="no-result">找不到符合頁面，試試其他術語。</p>';
}
function normalize(base,target){const stack=base.split('/');stack.pop();for(const part of target.split('/')){if(part==='..')stack.pop();else if(part!=='.'&&part)stack.push(part);}return stack.join('/');}
function renderText(text){const formulas=[];let protectedText=text.replace(/\$\$([\s\S]*?)\$\$/g,(_,tex)=>{const token=`WIKIMATHBLOCK${formulas.length}END`;formulas.push({token,tex,display:true});return '\n\n'+token+'\n\n';});
 protectedText=protectedText.replace(/(?<!\\)\$([^$\n]+?)\$/g,(_,tex)=>{const token=`WIKIMATHINLINE${formulas.length}END`;formulas.push({token,tex,display:false});return token;});
 let html=md.render(protectedText);for(const f of formulas){let rendered;try{rendered=katex.renderToString(f.tex,{displayMode:f.display,throwOnError:true,strict:'error'});}catch(e){rendered='<span class="math-error">公式錯誤：'+escape(e.message)+'</span>';}
 if(f.display)html=html.replace('<p>'+f.token+'</p>','<div class="math-display">'+rendered+'</div>');else html=html.replaceAll(f.token,rendered);}return html;}
function show(){let requested=new URLSearchParams(location.hash.slice(1)).get('p')||'wiki/index.md';const p=pages.get(requested);current=p?requested:'wiki/index.md';
 const page=pages.get(current);document.title=page.title+' · 3D 重建 Wiki';document.getElementById('breadcrumb').textContent='LLM Wiki / '+group(page)+' / '+page.path;
 document.getElementById('page-meta').textContent=current.startsWith('labs/')?'互動理解 · 模型假設與來源另列':'七章課程 Wiki · 2026.11.22 · 推導／案例／疑點可追溯';
 const content=document.getElementById('content');content.innerHTML=(p?'':'<blockquote>找不到指定頁面，已回到首頁。</blockquote>')+renderText(page.body);
 for(const a of content.querySelectorAll('a')){const href=a.getAttribute('href');if(!href||/^(https?:|mailto:|#)/.test(href))continue;const [target]=href.split('#');const resolved=normalize(page.path,target);if(pages.has(resolved))a.href='#p='+encodeURIComponent(resolved);else a.href=resolved;}
 const toc=document.getElementById('toc');toc.innerHTML='';let n=0;for(const h of content.querySelectorAll('h2,h3')){h.id='section-'+(++n);const a=document.createElement('a');a.href='#'+h.id;a.textContent=h.textContent;a.addEventListener('click',e=>{e.preventDefault();h.scrollIntoView({behavior:'smooth'});h.tabIndex=-1;h.focus({preventScroll:true});});toc.append(a);}
 for(const table of content.querySelectorAll('table')){const wrap=document.createElement('div');wrap.className='table-scroll';wrap.tabIndex=0;wrap.setAttribute('aria-label','可水平捲動表格');table.replaceWith(wrap);wrap.append(table);}
 const walker=document.createTreeWalker(content,NodeFilter.SHOW_TEXT,{acceptNode(node){return node.parentElement.closest('.katex,pre,code,a')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT;}});const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
 for(const node of nodes){const parts=node.nodeValue.split(/(\[(?:S\d{2}|E\d{2})[^\]\n]*\])/g);if(parts.length===1)continue;const frag=document.createDocumentFragment();for(const part of parts){if(/^\[(S\d{2}|E\d{2})/.test(part)){const a=document.createElement('a');a.className='source-ref';a.href='#p=wiki/sources.md';a.textContent=part;a.title='查看來源索引';frag.append(a);}else frag.append(document.createTextNode(part));}node.replaceWith(frag);}
 if(window.WikiLabs)window.WikiLabs.mount(content,page);
 drawNav();document.body.classList.remove('menu-open');document.getElementById('menu').setAttribute('aria-expanded','false');window.scrollTo(0,0);
}
document.querySelector('.skip').addEventListener('click',e=>{e.preventDefault();document.getElementById('main').focus();document.getElementById('main').scrollIntoView();});search.addEventListener('input',drawNav);window.addEventListener('hashchange',show);document.getElementById('menu').addEventListener('click',()=>{const open=document.body.classList.toggle('menu-open');document.getElementById('menu').setAttribute('aria-expanded',String(open));});show();
})();
