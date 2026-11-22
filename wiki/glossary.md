# 術語與符號速查

| 中文／英文 | 符號或縮寫 | 注意事項 | 來源 |
| --- | --- | --- | --- |
| 攝影測量 Photogrammetry | PM | 本課含物理影像單位與向後光軸慣例 | S02 pp.3,5,10 |
| 電腦視覺 Computer Vision | CV | 本課 K 以 pixel 表示，光軸向前 | S02 pp.4,10,16 |
| 相機率定 Camera Calibration | — | 求相機幾何與附加參數 | S02 pp.18,27–38 |
| 像主點 Principal Point | PM 的 $(x_p,y_p)$；CV 的 $(c_x,c_y)$ | 與影像中心、攝影中心區分 | S02 pp.13,17–18 |
| 像元尺寸 Pixel Size | $s,s_x,s_y$ | mm/pixel；不可與 skew 或齊次尺度混用 | S02 pp.12,15,18 |
| 偏斜 Skew | $\gamma$；表格亦有 s | 本 Wiki 各頁明訂符號 | S02 pp.15–18,37 |
| 徑向畸變 Radial Distortion | $K_i$ 或 $k_i$ | 係數需連同單位及映射方向 | S02 pp.23,26 |
| 偏心／切向畸變 Decentering / Tangential Distortion | $P_i$ 或 $p_i$ | 不直接視為同順序同定義 | S02 pp.24–27；E01 |
| 自率光束法 Self-Calibration | — | 沿用課程分類，避免與其他文獻混稱 | S02 pp.30–37 |
| 在任率定 On-the-job Calibration | — | 任務影像中估參 | S02 p.38 |
| 重投影誤差 Reprojection Error | 本 Wiki 用 $\Delta u,\Delta v$ | RMSE 須聲明每點或每分量 | S02 p.35；補充 |

[來源索引](sources.md) · [章節導覽](chapters/02-calibration.md)

## 其餘章節術語
| 中文／英文 | 定義與符號提醒 | 來源 |
| --- | --- | --- |
| 地面取樣間距 Ground Sampling Distance | GSD，物方長度／pixel | S01 pp.61–65 |
| 視場角 Field of View | FOV，角度 | S01 pp.61,65 |
| 相似／仿射／透視 Similarity / Affine / Projective | 4／6／8 自由度，條件不同 | S03 pp.7–18 |
| 殘差 Residual | 先定義觀測減模型或反向 | S03 pp.29–32 |
| 描述子 Descriptor | 編碼局部特徵，不是坐標本身 | S04 pp.41–47 |
| 隨機抽樣一致 Random Sample Consensus | RANSAC，在指定模型／門檻下選一致點 | S04 p.50 |
| 共線條件 Collinearity | 物點、攝影中心與理想像點共線 | S05 pp.18–24 |
| 前方／後方交會 Intersection / Resection | 求物點／求相機，條件不同 | S05 pp.26–28 |
| 基本／本質矩陣 Fundamental / Essential | F 作用於像素，E 作用於正規化射線 | S07 pp.8,17–24 |
| 核影像糾正 Stereo Rectification | 同名點到共同掃描列 | S07 pp.34–38 |
| 視差 Disparity | d，像方單位須與 f 一致 | S07 pp.36–39 |
| 半全局匹配 Semi-Global Matching | SGM，多路徑聚合的近似方法 | S07 pp.51–53 |
