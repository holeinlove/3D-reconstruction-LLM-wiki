# 感測器幾何：GSD 與視場角

## 概念、符號與條件
地面取樣間距（Ground Sampling Distance, GSD）描述一個像素在物方對應的長度；視場角（Field of View, FOV）描述可見角度。以下採理想針孔、光軸垂直平面、平坦目標及忽略畸變的模型。[S01 pp.60–65]

| 符號 | 定義 | 單位 |
| --- | --- | --- |
| H | 相機到目標平面垂直距離 | m |
| f | 焦距 | mm |
| s | 像元尺寸 | mm/pixel |
| W,Hpx | 水平／垂直像素數（Hpx 與距離 H 區分） | pixel |
| Sw,Sh | 感測器實體寬高 | mm |

## 教材公式與補齊推導
由相似三角形 $s/f=\mathrm{GSD}/H$：
$$
\mathrm{GSD}=\frac{Hs}{f},\qquad S_w=Ws,\quad S_h=H_{px}s.
$$
H 用 m、s 和 f 都用 mm，結果即 m/pixel。[S01 pp.61,63–64]

由中心到感測器邊界的直角三角形，半視角滿足 $\tan(\theta_w/2)=(S_w/2)/f$：
$$
\theta_w=2\tan^{-1}\frac{S_w}{2f},\qquad
\theta_h=2\tan^{-1}\frac{S_h}{2f}.
$$
**補充一致性驗算**：物方寬度 $L_w=2H\tan(\theta_w/2)=HS_w/f=W\,\mathrm{GSD}$。[S01 pp.61,65；代數補齊]

## 教材算例
6000×4000 pixel、s＝4 μm＝0.004 mm/pixel、f＝20 mm、H＝500 m：
$$
S_w=24\ \mathrm{mm},\ S_h=16\ \mathrm{mm},\quad
\mathrm{GSD}=500\times0.004/20=0.1\ \mathrm{m/pixel}.
$$
水平 FOV 約 61.93°、垂直約 43.60°；教材取約 62°×44°。p.65 的中間水平半角印成約 30.86°，依 $\arctan(12/20)$ 重算為約 30.96°；原近似不影響 62° 的最終整數，但在 I01-02 記錄。[S01 pp.63–65]

## 適用限制與疑點
p.64 寫 $\mathrm{GSD}_{oblique}=\mathrm{GSD}_{nadir}/\cos\theta$，又寫「越外圍越小」，式與文字趨勢不一致。傾斜成像的局部 GSD 還須指定方向、地形與角度定義，這條簡式不直接當通用公式。本 Wiki 的互動只實作上方垂直平面模型。[S01 p.64；I01-02]

感測器標稱「1/2 吋型」不是把英吋當普通長度換算；p.62 的 1.6 cm 是光學規格的歷史近似，實際尺寸應看廠商規格，不建立「1 inch＝1.6 cm」的單位規則。[S01 p.62；補充界線]

## 常見誤解
距離加倍，GSD 加倍但 FOV 不變；固定感測器與距離時，焦距加倍會使 GSD 減半、FOV 變小。較小 GSD 只是較細的取樣間距，不等於已證明量測準確度。

## 來源與相關頁
[互動：GSD 與視角](../../labs/index.md) · [來源](../sources.md) · [品質](sensing-quality.md) · [HW1](../cases/hw1-camera.md)
