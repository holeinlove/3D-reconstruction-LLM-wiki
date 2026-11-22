# 第 03 章：平面影像轉換

狀態：**已匯入，保留定義差異註記**。S03 共 54 張。

## 複習路線
| 投影片 | 重點 | 知識頁 |
| --- | --- | --- |
| pp.3–18 | 相似 4、仿射 6、透視 8 自由度及多項式 | [平面轉換](../concepts/planar-transforms.md) |
| pp.19–25 | 穩定、套合、拼接及 HW3 | [HW3 案例](../cases/hw3-stitching.md) |
| pp.26–34 | 設計矩陣、法方程式、殘差／自由度 | [最小二乘](../concepts/least-squares.md) |
| pp.35–54 | 陣列索引、正反算、最鄰近／雙線性／雙三次 | [內插推導](../concepts/interpolation.md) |

## 先修與應用
先讀 [第 02 章](02-calibration.md) 的座標與畸變。估計轉換模型所需對應點，來自 [第 04 章](04-matching.md)；一般三維場景的幾何模型則看 [第 05 章](05-collinearity.md)。[S03 pp.18–25]

## 互動與常見誤解
[平面變換與雙線性內插互動](../../labs/index.md)。請區分座標軸旋轉與點旋轉、仿射與透視，以及課堂自由度校正殘差與每點 RMSE，詳見[疑點](../issues.md)。

## 來源
[來源索引](../sources.md) · [Wiki 首頁](../index.md)
