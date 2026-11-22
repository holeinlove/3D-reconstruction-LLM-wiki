# 第 07 章：核幾何與立體視覺

狀態：**已匯入，保留模型與誤差條件註記**。S07 共 54 張。

## 複習路線
| 投影片 | 問題 | 知識頁 |
| --- | --- | --- |
| pp.3–8 | 極點、極線、極平面如何限制搜尋？ | [核幾何](../concepts/epipolar-geometry.md) |
| pp.10–22 | 內外積、齊次座標如何得到 F？ | [F 推導](../concepts/epipolar-geometry.md) |
| pp.24–32 | 如何由 E 求 R、t，為何尺度未知？ | [SVD 分解](../concepts/essential-decomposition.md) |
| pp.34–39 | 糾正後如何由視差算深度及誤差？ | [深度推導](../concepts/stereo-depth.md) |
| pp.40–49 | 光學測距、雙目系統與 ToF 案例 | [深度](../concepts/stereo-depth.md)、[HW4](../cases/hw4-stereo.md) |
| pp.51–54 | SGM／SGBM 如何得到視差與點雲？ | [匹配代價](../concepts/stereo-matching.md)、[HW4](../cases/hw4-stereo.md) |

## 互動與常見誤解
[極線與雙目深度互動](../../labs/index.md)：先看「點映射到線」，再看校正平行系統的 Z＝Bf/d。F 不是影像到影像的 H；t 方向不等於已知公尺基線。

## 來源與疑點
[來源](../sources.md) · [I07-01～03](../issues.md) · [Wiki 首頁](../index.md)
