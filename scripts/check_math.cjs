const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..');const katex=require(path.join(root,'vendor/katex/katex.min.js'));
const md=require(path.join(root,'vendor/markdown-it.min.js'))({html:false});
const data=JSON.parse(fs.readFileSync(path.join(root,'site-data.json'),'utf8'));let count=0,errors=[];
for(const p of data.pages){
 const withoutCode=p.body.replace(/```[\s\S]*?```/g,'');
 const block=/\$\$([\s\S]*?)\$\$/g;const inline=/(?<!\\)\$([^$\n]+?)\$/g;
 for(const m of withoutCode.matchAll(block)){count++;try{katex.renderToString(m[1],{displayMode:true,throwOnError:true,strict:'error'});}catch(e){errors.push({page:p.path,formula:m[1],error:e.message});}}
 for(const m of withoutCode.replace(block,'').matchAll(inline)){count++;try{katex.renderToString(m[1],{throwOnError:true,strict:'error'});}catch(e){errors.push({page:p.path,formula:m[1],error:e.message});}}
 try{md.render(p.body);}catch(e){errors.push({page:p.path,error:e.message});}
}
const report={date:'2026-11-22',passed:errors.length===0,formula_count:count,errors,limit:'TeX syntax and Markdown rendering only; not proof of mathematical correctness'};
fs.writeFileSync(path.join(root,'reports/math-check.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2));process.exitCode=errors.length?1:0;
