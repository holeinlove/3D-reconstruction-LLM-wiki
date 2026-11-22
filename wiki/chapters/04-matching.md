# 第 04 章：影像匹配

狀態：**已匯入**。S04 共 52 張；三個階段要分清楚：偵測 → 描述／配對 → 幾何驗證。

## 複習路線
| 投影片 | 問題 | 知識頁 |
| --- | --- | --- |
| pp.3–20 | 角點、FAST、DoG 各偵測什麼？ | [偵測與推導](../concepts/feature-detection.md) |
| pp.21–32 | 邊緣如何變成線與線段？ | [Canny／Hough／LSD](../concepts/feature-detection.md) |
| pp.33–48 | 區域與描述子如何找對應？ | [NCC 與比率測試](../concepts/feature-matching.md) |
| pp.49–50 | 如何排除幾何不一致？ | [RANSAC](../concepts/robust-estimation.md) |
| pp.51–52 | 匹配如何接到相機姿態與三維點？ | [SfM 案例](../cases/sfm-pipeline.md) |

## 互動與跨章
[比率測試／RANSAC 互動](../../labs/index.md)。第 03 章提供平面模型，第 06 章提供異質資料案例，第 07 章提供雙視圖幾何；對應點只是觀測，仍需正確模型。[S04 pp.3,50–51]

## 來源與疑點
[來源](../sources.md) · [I04-01 Canny 方向](../issues.md) · [Wiki 首頁](../index.md)
