# 相機內參與針孔投影

## 概念
內方位參數（Intrinsic Parameters / Interior Orientation Parameters, IOPs）描述相機內部的投影幾何；外方位參數（Extrinsic Parameters）描述世界與相機的相對位置及姿態。畸變係數是理想針孔模型之外的附加參數。[S02 pp.8–9,18,27]

## 符號與單位
| 符號 | 定義 | 單位 |
| --- | --- | --- |
| $f$ | 主距／課程稱焦距 | mm |
| $s_x,s_y$ | 水平、垂直像元尺寸 | mm/pixel |
| $f_x=f/s_x,\ f_y=f/s_y$ | 像素焦距 | pixel |
| $(c_x,c_y)$ | CV 主點 | pixel |
| $\gamma$ | 教材 p.15 的 skew 項 | pixel |
| $(x',y')$ | 正規化相機座標 | 無因次 |
| $\lambda$ | 本頁新增的齊次尺度符號 | 與所選齊次表示有關 |

教材在不同表格亦以 s 表 skew；此頁採 p.15 的 $\gamma$ 避免與像元尺寸混淆。[S02 pp.15–18,37]

## 教材公式與關鍵推導
在 CV 前方像平面、$Z_c\ne0$ 的約定下，相似三角形給出：
$$
x=f\frac{X_c}{Z_c},\qquad y=f\frac{Y_c}{Z_c}.
$$
除以 $f$ 得正規化座標 $x'=X_c/Z_c,\ y'=Y_c/Z_c$。此段 $(x,y)$ 指 CV 虛擬像平面的連續座標，與 PM 頁的方向不同。[S02 p.14]

換成像素並加上主點：
$$
u=f_xx'+\gamma y'+c_x,\qquad v=f_yy'+c_y.
$$
$$
K=\begin{bmatrix}f_x&\gamma&c_x\\0&f_y&c_y\\0&0&1\end{bmatrix},\qquad
\lambda\begin{bmatrix}u\\v\\1\end{bmatrix}=K\begin{bmatrix}X_c\\Y_c\\Z_c\end{bmatrix}.
$$
[S02 pp.15–16]

**補充推導**：將 $x',y'$ 代入矩陣式，再乘 $Z_c$ 即得齊次形式；此選法可取 $\lambda=Z_c$。本頁用 $\lambda$ 區分教材像元尺寸 $s$，不是改變模型。

## 自建算例
假設 $f=20\,\mathrm{mm}$、$s_x=s_y=0.005\,\mathrm{mm/pixel}$，則 $f_x=f_y=4000\,\mathrm{pixel}$。這是用來驗算單位的假設例子，不是教材實測率定結果。

## 假設與適用條件
這是無畸變的針孔模型；畸變不包含在 K 本身。$\gamma=0$ 是常用簡化，不應把非零 skew 的式子直接當作所有工具都支援的估計選項。[S02 pp.15–16,20–27；E01 Detailed Description 查核]

## 常見誤解
內參 K 已知，不代表物點深度已知；一個像素仍對應一條觀測射線。mm 的 f 不可直接填入以 pixel 為單位的 K。[S02 pp.11,14–19；補充推論]

## 來源與相關頁
[來源索引](../sources.md) · [座標](coordinate-systems.md) · [畸變](distortion.md) · [棋盤格](checkerboard.md)
