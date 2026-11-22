# 影像感測與 3D 場景重建

七份課堂教材的個人複習 Wiki：**7／7 份已匯入，共 437 張投影片的去向對照**。保留關鍵推導、案例、來源與待查項；不把資料缺漏或模型算例當成實測成果。初學者教學 HTML 簡報仍為後續任務。

## 先動手理解
[開啟互動學習實驗室](../labs/index.md)：GSD／FOV、徑向畸變、平面轉換、雙線性內插、比率測試／RANSAC、匹配指標、旋轉與投影、點到極線、雙目深度／誤差。九個模組均可調參、重設並回到公式來源。

## 依課程章節複習
| 章節 | 學習問題 |
| --- | --- |
| [01 影像感測器](chapters/01-sensors.md) | 成像品質、解析度、曝光與感測幾何 |
| [02 相機率定](chapters/02-calibration.md) | 座標、內參、畸變與率定 |
| [03 平面影像轉換](chapters/03-planar.md) | 模型、參數估計與內插 |
| [04 影像匹配](chapters/04-matching.md) | 偵測、描述、配對與幾何驗證 |
| [05 空間轉換與共線條件式](chapters/05-collinearity.md) | 旋轉、投影、交會與平差 |
| [06 影像匹配之應用](chapters/06-applications.md) | 多光譜、拼接、學習式匹配與定位 |
| [07 核幾何](chapters/07-epipolar.md) | F／E、視差、深度與立體匹配 |

## 依概念查詢
**成像與相機**：[品質／曝光](concepts/sensing-quality.md)、[GSD／FOV](concepts/sensor-geometry.md)、[鏡頭／多波段](concepts/camera-optics.md)、[座標](concepts/coordinate-systems.md)、[內參](concepts/intrinsics.md)、[畸變](concepts/distortion.md)、[率定方法](concepts/calibration-methods.md)、[棋盤格](concepts/checkerboard.md)、[修正](concepts/undistortion.md)。

**對位與匹配**：[平面模型](concepts/planar-transforms.md)、[最小二乘](concepts/least-squares.md)、[內插](concepts/interpolation.md)、[偵測](concepts/feature-detection.md)、[NCC／描述子](concepts/feature-matching.md)、[RANSAC](concepts/robust-estimation.md)、[指標](concepts/matching-metrics.md)、[多光譜套合](concepts/multispectral-registration.md)、[學習式匹配](concepts/learned-matching.md)。

**三維重建**：[旋轉](concepts/spatial-rotation.md)、[共線／DLT](concepts/collinearity.md)、[交會／方位／平差](concepts/orientation-adjustment.md)、[核幾何 F](concepts/epipolar-geometry.md)、[E／SVD](concepts/essential-decomposition.md)、[雙目深度](concepts/stereo-depth.md)、[立體匹配](concepts/stereo-matching.md)。

## 案例與作業導引
[HW1 取像](cases/hw1-camera.md) · [主點算例](cases/principal-point.md) · [HW2 率定](cases/hw2-calibration.md) · [HW3 拼接](cases/hw3-stitching.md) · [SfM](cases/sfm-pipeline.md) · [陣列拼接](cases/multi-camera-stitch.md) · [UAV 地理對位](cases/geographic-registration.md) · [工程量測](cases/engineering-measurement.md) · [HW4 立體點雲](cases/hw4-stereo.md)。

## 來源、流程與真實紀錄
[術語](glossary.md) · [來源索引](sources.md) · [疑點台帳](issues.md) · [流程 Graph](../workflow/graph.md) · [本次六章匯入與互動驗收](../reports/course-import.md) · [初次試做歷史紀錄](../reports/pilot-02.md) · [日誌](log.md)。

## 初學者教學簡報
[開啟七章 HTML 簡報首頁](../slides/index.html)：依第 01～07 章選課，進入各章互動教學。另有[課程總覽與作業流程](../slides/overview.html)，保留來源對應、Loop／Graph、實際檢查與反思。[七章驗收](../reports/chapters-check.md)。
