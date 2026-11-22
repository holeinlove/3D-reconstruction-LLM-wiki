# 第 02 章：相機率定

狀態：**試做，待使用者確認整理方式**。來源 S02，共 44 張投影片。

相機率定（Camera Calibration）的用途，是估計相機成像幾何與畸變參數，使影像能用於後續幾何量測。[S02 pp.8,18,20–31]

## 複習路線
| 教材位置 | 要回答的問題 | 知識頁 |
| --- | --- | --- |
| pp.2–5 | PM 與 CV 的課程觀點有何差異？ | [座標與慣例](../concepts/coordinate-systems.md) |
| pp.7–19 | 物點如何變成像素？負號與單位從哪裡來？ | [座標系統](../concepts/coordinate-systems.md)、[相機內參](../concepts/intrinsics.md) |
| pp.20–27 | 徑向與切向畸變如何表示？係數能否直接通用？ | [鏡頭畸變](../concepts/distortion.md) |
| pp.28–38 | 實驗室、自率、在任率定有何差異？ | [率定方法](../concepts/calibration-methods.md)、[棋盤格推導](../concepts/checkerboard.md) |
| pp.39–43 | 參數變動及修正方向如何處理？ | [影像修正](../concepts/undistortion.md) |
| p.44 | HW2 要做什麼、還缺哪些實驗資料？ | [HW2 案例](../cases/hw2-calibration.md) |

## 本章必須分清楚的三件事
1. 影像幾何中心、像主點與三維攝影中心不同。[S02 pp.9,12–18]
2. PM 的 mm 與 CV 的 pixel／正規化座標，不可直接代入同一係數。[S02 pp.12–19,26]
3. 求得參數、修正影像、重新率定是三項不同工作。[S02 pp.28–44]

## 建議閱讀順序
座標 → 內參 → [主點算例](../cases/principal-point.md) → 畸變 → 率定方法 → 棋盤格 → 影像修正 → HW2。

## 本章待查事項
第 25／31 頁切向公式的平方項係數、第 26／31／42 頁修正量方向、第 13 頁主點用語，以及第 37 頁精度比較，都保留在[疑點台帳](../issues.md)。未解項不作後續簡報定論。

## 來源與相關頁
[來源索引](../sources.md) · [術語](../glossary.md) · [Wiki 首頁](../index.md)
