# 來源索引

## 課堂教材
作者：詹鈞評，國立臺灣科技大學人工智慧跨域科技研究所。頁碼一律採 PowerPoint 實體投影片順序，含封面，不依擷取文字中的頁碼推算。

| ID | 教材 | 頁數 | 狀態 |
| --- | --- | --- | --- |
| S01 | 01 影像感測器 | 104 | 已匯入 |
| S02 | 02 相機率定 | 44 | 已完成本次試做整理，待使用者確認 |
| S03 | 03 平面影像轉換 | 54 | 已匯入 |
| S04 | 04 影像匹配 | 52 | 已匯入 |
| S05 | 05 空間轉換與共線條件式 | 61 | 已匯入 |
| S06 | 06 影像匹配之應用 | 68 | 已匯入 |
| S07 | 07 核幾何 | 54 | 已匯入 |

原始檔名與 S02 雜湊見 [catalog.json](../sources/catalog.json)，全七章逐頁去向見 [coverage.json](../sources/coverage.json)。未公開原始教材，本頁不提供假裝可下載的連結。

## 外部查核（僅輔助，不取代教材）
- **E01**：[OpenCV 4.13.0 幾何模組](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html)，Detailed Description。核對 normalized coordinates、K 與畸變參數慣例。
- **E02**：[OpenCV 4.13.0 率定教學](https://docs.opencv.org/4.13.0/dc/dbb/tutorial_py_calibration.html)，Basics、Code、Re-projection Error。核對角點、影像修正與重投影概念。
- **E03**：[Zhang 原始技術報告](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr98-71.pdf)，§2.2–2.3、§3.1–3.3。核對平面單應性、旋轉正交約束及非線性最佳化。課堂 p.35 引用的是 Zhang (2000)，此處連到作者官方技術報告版本，版本不可混稱。

以上查閱日均為 2026-11-22。每頁以 E01／E02／E03 標記外部補充；算例另註來源或自建。

## 第二階段外部查核
- **E04**：[OpenCV Homography](https://docs.opencv.org/4.13.0/d9/dab/tutorial_homography.html)，Basic theory：平面映射、八自由度與適用情境。查閱日 2026-11-22。

- **E06**：[LightGlue 官方專案](https://github.com/cvg/LightGlue)，README 的 adaptive depth／width 與 feature matching 定義。
- **E07**：[SuperGlue 官方專案](https://github.com/magicleap/SuperGluePretrainedNetwork)，README 的模型角色與 graph／optimal matching。查閱日 2026-11-22。

- **E05**：[OpenCV Epipolar Geometry](https://docs.opencv.org/4.13.0/da/de9/tutorial_py_epipolar_geometry.html)，Basic concepts／Code：點到極線、F／E 角色與八點法語境。查閱日 2026-11-22。

- **E08**：[OpenCV StereoSGBM](https://docs.opencv.org/4.13.0/d2/d85/classcv_1_1StereoSGBM.html)，Detailed Description／create：P1、P2、修改型代價與視差尺度。查閱日 2026-11-22。
