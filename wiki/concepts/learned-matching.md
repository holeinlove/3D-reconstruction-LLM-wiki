# 學習式匹配：SuperPoint、SuperGlue 與 LightGlue

## 定義與角色
SuperPoint 偵測特徵位置、分數並輸出描述子；SuperGlue／LightGlue 則以兩圖的局部特徵作匹配。三者角色與架構不同，不能把 detector 與 matcher 當成同一模型。[S06 pp.42–58；E06／E07 官方查核]

## 形狀、符號與推導
教材 SuperPoint 共享 encoder 將 H×W 影像轉成約 H/8×W/8 的粗特徵。偵測分支 65 通道對應一個 8×8 cell 的 64 位置與一個 dustbin；去掉 dustbin 並重排可形成 H×W 分數圖。**補充**：這是每位置分數，不代表每 cell 永遠只能保留一個最終 keypoint，還須門檻及非極大值抑制等步驟。[S06 pp.43–48；I06-02]

描述分支為 H/8×W/8×D，教材 D＝256；經插值與 L2 正規化形成描述。正規化後向量為無因次，輸出座標的縮放仍須對應原圖。[S06 pp.47–49]

SuperGlue 在同圖做 self-attention、跨圖做 cross-attention，更新後描述子計算：
$$
S_{ij}=\langle f_i^A,f_j^B\rangle,\qquad S\in\mathbb R^{M\times N}.
$$
加入不能匹配的 dustbin 列／欄成 (M+1)×(N+1)，再以最佳匹配層（教材 Sinkhorn 示意）形成部分分配矩陣 P。P 不是三維空間點座標。[S06 pp.50–58]

## 外部查核與教材混用
LightGlue 官方專案明確提供自適應深度／寬度的匹配機制；SuperGlue 官方專案則對應圖神經網路與最優傳輸匹配。p.42 標題 LightGlue、內文／圖 SuperGlue，p.59 又列 LightGlue 門檻，故本 Wiki 分開說明，不能把 pp.50–58 的架構直接標成 LightGlue。[S06 pp.42,50–59；E06／E07；I06-02]

## 案例、條件與常見誤解
空拍與衛星資料有尺度、時間、季節差異；學習式匹配提供候選，但仍要轉成地理三維控制點並檢查後方交會結果。匹配信心分數不是定位誤差的公尺數，也不能跨模型直接比較。[S06 pp.35–42,59–68]

## 來源與相關頁
[來源](../sources.md) · [地理對位案例](../cases/geographic-registration.md) · [傳統描述子](feature-matching.md) · [疑點](../issues.md)
