# 空間旋轉：順序、方向與正交性

## 定義與符號
教材以 ω（Omega）、φ（Phi）、κ（Kappa）表示繞 X、Y、Z 軸的角度。M 是物空間到像空間，R 是反向。列向量與右乘順序固定後，先做的矩陣在最右側；這裡是課堂的座標轉換慣例，不混用另一套 active rotation 的正號。[S05 pp.3–15]

## 教材矩陣與推導
依 pp.6–8 的分步矩陣：
$$
M_\omega=\begin{bmatrix}1&0&0\\0&\cos\omega&\sin\omega\\0&-\sin\omega&\cos\omega\end{bmatrix},\quad
M_\varphi=\begin{bmatrix}\cos\varphi&0&-\sin\varphi\\0&1&0\\\sin\varphi&0&\cos\varphi\end{bmatrix},
$$
$$
M_\kappa=\begin{bmatrix}\cos\kappa&\sin\kappa&0\\-\sin\kappa&\cos\kappa&0\\0&0&1\end{bmatrix}.
$$
$$
\mathbf X_1=M_\omega\mathbf X_0,\quad
\mathbf X_2=M_\varphi\mathbf X_1,\quad
\mathbf X_3=M_\kappa\mathbf X_2=M_\kappa M_\varphi M_\omega\mathbf X_0.
$$
pp.9、11 的展開欄可與此乘積核對；p.9 上方 κ 子矩陣符號卻與 p.8／p.11 不一致，列 I05-01。互動採 pp.6–8 與 p.11 一致的定義。[S05 pp.5–13]

## 反向與幾何條件
各基本矩陣正交，所以 $M^TM=I$，且：
$$
R=M^{-1}=M^T=M_\omega^TM_\varphi^TM_\kappa^T.
$$
矩陣元素無因次、點坐標可用 m 或 mm；輸入角在程式中需轉 radian。旋轉還須 $\det M=+1$；只有正交性也可能包含鏡射。[S05 pp.10–13；det 條件補充]

## 補充算例與常見誤解
ω＝φ＝κ＝0 時 M＝I；κ＝90° 時 (1,0,0) 變為 (0,−1,0)，這與本課被動軸向相符。一般 $M_\kappa M_\omega\ne M_\omega M_\kappa$，交換順序不能只把角名互換。[S05 pp.4–13；自建驗算]

## 應用與條件
Roll／Pitch／Yaw 必須先指定載具軸與參考方向，再連到 ω／φ／κ。參考座標、角度順序、轉換方向與長度單位應隨參數一起保存。[S05 p.15；補充操作規則]

## 來源與相關頁
[來源](../sources.md) · [互動旋轉與投影](../../labs/index.md) · [共線推導](collinearity.md) · [座標慣例](coordinate-systems.md)
