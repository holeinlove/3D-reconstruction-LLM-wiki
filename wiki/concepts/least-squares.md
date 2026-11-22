# 最小二乘、殘差與精度定義

## 定義與符號
最小二乘（Least Squares）在選定模型與觀測下，找使殘差平方和最小的參數。教材 $L=AX+V$ 與後頁 $V=AX-L$ 有符號差異，但平方和與解不受整體變號影響。本頁固定 $v=A\theta-L$；$\theta$ 是為避免參數 X 與目標座標 X 混淆而新增的符號。[S03 pp.27–32]

## 推導
$$
J(\theta)=v^Tv=(A\theta-L)^T(A\theta-L).
$$
$$
\frac{\partial J}{\partial\theta}=2A^T(A\theta-L)=0
\quad\Longrightarrow\quad A^TA\hat\theta=A^TL.
$$
若 A 滿列秩，$\hat\theta=(A^TA)^{-1}A^TL$。教材 p.30 導數印出負號但仍得到同一個零點方程；正文保留一致推導，原述在 I03-02。**實作補充**：QR／SVD 解最小二乘通常比直接形成反矩陣更合適；此頁反矩陣用來說明代數。[S03 pp.29–30]

## 仿射設計矩陣
$$
\begin{bmatrix}X_i\\Y_i\end{bmatrix}=
\begin{bmatrix}1&x_i&y_i&0&0&0\\0&0&0&1&x_i&y_i\end{bmatrix}
\begin{bmatrix}a_0\\a_1\\a_2\\b_0\\b_1\\b_2\end{bmatrix}+\text{殘差}.
$$
每個對應點提供兩列，n 點共 2n 條觀測，未知數六個。上式殘差採「觀測減模型」；若用本頁 v，將殘差移至另一側即可，平方和相同。[S03 pp.31–32；符號整理]

## RMSE 與自由度
教材把 $\sqrt{v^Tv/(N_v-N_x)}$ 稱 RMSE；仿射案例分母為 $2n-6$。本 Wiki 明稱「自由度校正殘差尺度」，並與每點二維 RMSE 分開：
$$
\hat\sigma_0=\sqrt{\frac{v^Tv}{2n-6}},\qquad
\mathrm{RMSE}_{point}=\sqrt{\frac{v^Tv}{n}}.
$$
**補充算例**：n＝5、SSE＝2 pixel²，前者 $\sqrt{2/4}=0.7071$ pixel，後者 $\sqrt{2/5}=0.6325$ pixel。不是同一統計量；n＝3 時前者分母為零，不能報零誤差尺度。[S03 pp.30,32；自建數值驗算]

## 案例、限制與常見誤解
誤差向量圖能顯示周邊系統偏差；只報單一總 RMSE 會遮住空間模式。更多參數可能降低訓練點殘差，但不保證新點精度。理論最少點數不代表已有穩定冗餘觀測。[S03 pp.18,25,28,34；補充判讀]

## 來源與相關頁
[來源](../sources.md) · [平面轉換](planar-transforms.md) · [HW3](../cases/hw3-stitching.md) · [率定 RMSE 算例](checkerboard.md)
