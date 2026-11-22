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
