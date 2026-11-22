# 平面轉換：相似、仿射與單應性

## 定義與符號
將平面點 (x,y) 映成 (X,Y)。本頁兩者都用同一影像長度單位（pixel）；平移也用 pixel，尺度與剪切無因次，角度在計算時用 radian。[S03 pp.3–18]

## 教材公式與關鍵推導
相似轉換（Similarity）保形與角度：
$$
X=a_0+m(x\cos\alpha-y\sin\alpha),\quad
Y=b_0+m(x\sin\alpha+y\cos\alpha).
$$
令 $a_1=m\cos\alpha,\ b_1=m\sin\alpha$，可寫為 $X=a_0+a_1x-b_1y,\ Y=b_0+b_1x+a_1y$，共有四參數。兩個不同點提供四條觀測式，但不能退化為同一點。[S03 pp.7–9,18；中間代換補齊]

仿射轉換（Affine）：
$$
X=a_0+a_1x+a_2y,\qquad Y=b_0+b_1x+b_2y.
$$
可含非等向縮放與剪切，保持共線性及平行性；六參數最少需三組不共線對應。寫成 $\mathbf X=A\mathbf x+t$，可逆須 $\det A\ne0$。[S03 pp.10–13,18；可逆條件補充]

透視轉換（Projective / Homography）：
$$
X=\frac{a_0+a_1x+a_2y}{1+c_1x+c_2y},\qquad
Y=\frac{b_0+b_1x+b_2y}{1+c_1x+c_2y}.
$$
$$
\lambda\begin{bmatrix}X\\Y\\1\end{bmatrix}=
\begin{bmatrix}a_1&a_2&a_0\\b_1&b_2&b_0\\c_1&c_2&1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}.
$$
分母移項得 $X=a_0+a_1x+a_2y-Xxc_1-Xyc_2$，對未知係數可建線性初估系統。八自由度一般位置下至少四對；固定右下為 1 只適用該元素非零的尺度選法。[S03 pp.14–15,18；E04 Basic theory 補充界線]

## 二次多項式
課堂以 $a_{00},a_{10},a_{11},a_{20},a_{21},a_{22}$ 表示 $1,x,y,x^2,xy,y^2$ 六項（Y 使用 b）。每軸六係數，可描述彎曲，但需足夠且分布良好的控制點，不能自動視為物理相機模型。[S03 p.16]

## 條件與常見誤解
單一 H 可用於平面場景，或特定純旋轉成像等條件；一般有深度差及相機平移的場景不會全部由一個 H 精確對齊。Homography 不是 Affine 的同義詞；令 $c_1=c_2=0$ 才回到仿射形式。[S03 pp.14–18；E04]

p.5 的 $\left[\begin{smallmatrix}\cos\alpha&\sin\alpha\\-\sin\alpha&\cos\alpha\end{smallmatrix}\right]$ 描述座標軸旋轉；p.7 的點變換是另一方向，不能省略方向解釋。互動模組沿本頁 p.7 點變換約定。[S03 pp.5,7；I03-01]

## 案例與相關頁
[HW3 拼接](../cases/hw3-stitching.md) · [互動平面轉換](../../labs/index.md) · [最小二乘](least-squares.md) · [來源](../sources.md)
