# 特徵偵測：角點、斑點、邊緣與線段

## 定義與符號
特徵偵測（Feature Detection）找穩定、可重複且具區別性的位置；「偵測到點」不等於已找到跨影像對應。I 為灰階值，x,y 為影像位置，$I_x,I_y$ 為梯度，窗口權重 w 與微小平移 u,v 另定義於下式。[S04 pp.3–6]

## Harris 的關鍵推導
教材以窗口平移前後強度差平方和判斷角點：
$$
E(u,v)=\sum_{x,y}w(x,y)[I(x+u,y+v)-I(x,y)]^2.
$$
泰勒一階 $I(x+u,y+v)-I(x,y)\approx I_xu+I_yv$，代入得：
$$
E(u,v)\approx [u\ v]M[u\ v]^T,\qquad
M=\sum_{x,y}w(x,y)\begin{bmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{bmatrix}.
$$
$$
R=\det M-k(\operatorname{tr}M)^2.
$$
M 的兩個特徵值都大，代表兩方向移動皆顯著改變灰階；一大一小偏向邊緣，皆小偏向平坦。教材 k 約 0.04–0.06，這不是跨影像通用的角點強度門檻。[S04 pp.7–11；泰勒中間步驟補齊]

## FAST 與 DoG
FAST 比較中心點周圍半徑 3 pixel 的 16 點，連續 N 點都高於 $I_p+t$ 或低於 $I_p-t$ 才形成候選；再做非極大值抑制。[S04 pp.12–14]

DoG 在不同尺度相減：
$$
L(x,y,\sigma)=G(x,y,\sigma)*I(x,y),\quad
D(x,y,\sigma)=L(x,y,k\sigma)-L(x,y,\sigma).
$$
在 (x,y,σ) 尺度空間找局部極值。k 為尺度倍率，不是 Harris 的 k；σ 單位為 pixel。DoG 是 SIFT 偵測的重要部分，不應把整個 SIFT／SURF／ORB 當成同一種角點算式。[S04 pp.15–20]

## 邊緣與線段
Canny：平滑 → 梯度 → 非極大值抑制 → 雙門檻與遲滯連結。教材 p.23 寫沿「邊緣方向」找極大；與 p.21 的梯度方向說明不同，實作應分清梯度法向與邊緣切向，疑點 I04-01 保留。[S04 pp.21–25]

Hough 將邊緣像素投票到 $\rho=x\cos\theta+y\sin\theta$ 參數空間；ρ 為 pixel，θ 為法線角。LSD（Line Segment Detector）從梯度方向一致的線支撐區域擬合有限線段，再用統計規則篩選。[S04 pp.26–32]

## 案例、條件與常見誤解
Harris／FAST 的基礎形式不具完整尺度不變性；旋轉／光照「穩定」也不是在任意曝光、遮蔽或透視下保證不變。重複紋理可能產生很多點，卻難以唯一配對。[S04 pp.5,11,14,19,40；補充界線]

## 來源與相關頁
[來源](../sources.md) · [描述與配對](feature-matching.md) · [幾何驗證](robust-estimation.md) · [SfM 案例](../cases/sfm-pipeline.md)
