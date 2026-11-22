/* Pure model functions, shared by the reader and numeric checks. */
(function(root,factory){if(typeof module==='object'&&module.exports)module.exports=factory();else root.WikiMath=factory();})(typeof globalThis!=='undefined'?globalThis:this,function(){
'use strict';
const rad=d=>d*Math.PI/180,transpose=A=>A[0].map((_,i)=>A.map(r=>r[i]));
const mul=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((v,a,k)=>v+a*B[k][j],0)));
const mv=(A,v)=>A.map(row=>row.reduce((s,a,i)=>s+a*v[i],0));
const det=A=>A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]);
function gsd(p){if(p.f<=0||p.h<=0||p.pixel<=0)return null;const s=p.pixel/1000;return {gsd:p.h*s/p.f,sw:p.width*s,sh:p.height*s,hfov:2*Math.atan(p.width*s/(2*p.f))*180/Math.PI,vfov:2*Math.atan(p.height*s/(2*p.f))*180/Math.PI,footprint:p.width*p.h*s/p.f};}
function planar(p){let a=rad(p.angle),sx=p.sx,sy=p.model==='similarity'?sx:p.sy,h=p.model==='similarity'?0:p.shear,k=p.model==='projective'?p.p:0,q=p.model==='projective'?p.q:0;const H=[[sx*Math.cos(a),-sy*Math.sin(a)+h,p.tx],[sx*Math.sin(a),sy*Math.cos(a),p.ty],[k,q,1]];const source=[[-80,-60],[80,-60],[80,60],[-80,60]];let den=source.map(([x,y])=>k*x+q*y+1);return {H,det:det(H),horizon:Math.min(...den)<=0&&Math.max(...den)>=0,points:source.map(([x,y],i)=>Math.abs(den[i])<1e-8?null:[(H[0][0]*x+H[0][1]*y+p.tx)/den[i],(H[1][0]*x+H[1][1]*y+p.ty)/den[i]])};}
function bilinear(p){const weights=[(1-p.dx)*(1-p.dy),p.dx*(1-p.dy),(1-p.dx)*p.dy,p.dx*p.dy];return {weights,value:weights.reduce((s,w,i)=>s+w*p.values[i],0)};}
function matching(p){let ratio=p.d2>0&&p.d1<=p.d2?p.d1/p.d2:null;let N=p.w<=0?null:p.w>=1?1:Math.ceil(Math.log1p(-.99)/Math.log1p(-Math.pow(p.w,p.sample)));return {ratio,accepted:ratio===null?null:ratio<p.tau,iterations:N};}
function metrics(p){if(p.m>Math.min(p.fa,p.fb)||p.duplicate>p.m||p.correct>p.m-p.duplicate)return null;return {mr:p.fa+p.fb>0?200*p.m/(p.fa+p.fb):null,dr:p.m>0?100*p.duplicate/p.m:null,cr:p.m>p.duplicate?100*p.correct/(p.m-p.duplicate):null};}
function rotation(p){let w=rad(p.omega),v=rad(p.phi),k=rad(p.kappa),cw=Math.cos(w),sw=Math.sin(w),cv=Math.cos(v),sv=Math.sin(v),ck=Math.cos(k),sk=Math.sin(k);let A=[[1,0,0],[0,cw,sw],[0,-sw,cw]],B=[[cv,0,-sv],[0,1,0],[sv,0,cv]],C=[[ck,sk,0],[-sk,ck,0],[0,0,1]];let M=mul(mul(C,B),A),q=mv(M,[p.x,p.y,-p.z]);let mm=mul(transpose(M),M),error=Math.max(...mm.flatMap((row,i)=>row.map((x,j)=>Math.abs(x-(i===j?1:0)))));return {M,q,det:det(M),orthogonality:error,visible:q[2]<-1e-8,image:q[2]<-1e-8?[-p.f*q[0]/q[2],-p.f*q[1]/q[2]]:null};}
function epipolar(p){let y=rad(p.yaw),c=Math.cos(y),s=Math.sin(y);let Kinv=[[1/300,0,-160/300],[0,1/300,-100/300],[0,0,1]],Rot=[[c,0,s],[0,1,0],[-s,0,c]],t=[-1,-.2,.1],cross=[[0,-t[2],t[1]],[t[2],0,-t[0]],[-t[1],t[0],0]];let F=mul(mul(transpose(Kinv),mul(cross,Rot)),Kinv),line=mv(F,[p.u,p.v,1]),norm=Math.hypot(line[0],line[1]);let samples=[3,5,10].map(z=>{let X=[(p.u-160)/300*z,(p.v-100)/300*z,z],q=mv(Rot,X).map((a,i)=>a+t[i]);return [300*q[0]/q[2]+160,300*q[1]/q[2]+100];});return {F,line,distance:norm>1e-12?Math.abs(line[0]*p.ru+line[1]*p.rv+line[2])/norm:null,samples};}
function stereo(p){if(p.d<=0||p.b<=0||p.f<=0)return {valid:false};return {valid:true,z:p.b*p.f/p.d,sigma:p.b*p.f/(p.d*p.d)*p.sigma};}
function distort(x,y,k){let r2=x*x+y*y;return [x*(1+k*r2),y*(1+k*r2)];}
return {rad,transpose,mul,mv,det,gsd,planar,bilinear,matching,metrics,rotation,epipolar,stereo,distort};
});
