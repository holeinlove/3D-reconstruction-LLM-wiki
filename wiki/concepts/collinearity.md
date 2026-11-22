# 共線條件式：三維物點到影像

## 定義、符號與單位
共線條件式（Collinearity Equation）要求理想像點、攝影中心及物點在同一直線。A＝$(X_A,Y_A,Z_A)$ 是物點，O＝$(X_O,Y_O,Z_O)$ 為攝影中心；M 將物空間方向轉到相機像空間；f、$x_p,y_p$、像點 x,y 用 mm，物方坐標可用 m，但分子分母須同單位。[S05 pp.16–23]

## 教材推導補齊
$$
\mathbf v_i=\begin{bmatrix}x_a-x_p\\y_a-y_p\\-f\end{bmatrix},\qquad
\mathbf v_o=\begin{bmatrix}X_A-X_O\\Y_A-Y_O\\Z_A-Z_O\end{bmatrix},\qquad
\mathbf v_i=\lambda M\mathbf v_o.
$$
令 $M\mathbf v_o=(q_1,q_2,q_3)^T$；由第三列 $-f=\lambda q_3$，所以 $\lambda=-f/q_3$，代入前兩列：
$$
x_a-x_p=-f\frac{m_{11}(X_A-X_O)+m_{12}(Y_A-Y_O)+m_{13}(Z_A-Z_O)}{m_{31}(X_A-X_O)+m_{32}(Y_A-Y_O)+m_{33}(Z_A-Z_O)},
$$
$$
y_a-y_p=-f\frac{m_{21}(X_A-X_O)+m_{22}(Y_A-Y_O)+m_{23}(Z_A-Z_O)}{m_{31}(X_A-X_O)+m_{32}(Y_A-Y_O)+m_{33}(Z_A-Z_O)}.
$$
這是無畸變的課堂 PM 形式。分母為零時無有限投影；物點還需在選定光軸的可見前方。不要把 CV 正向 Z 公式的正號直接搬來。[S05 pp.18–24；條件補充]

## 畸變與原式界線
p.23 在共線式右側加 Δx、Δy 表示附加項；其切向平方項含 2，與 S02 原式差異見 I01-03。加號是該頁的模型方向，與「由原始點加修正量」必須分開定義，不把它當已完成統一的軟體模型。[S05 p.23；S02 pp.26,31,42–43]

## DLT 與平面關係
直接線性轉換（Direct Linear Transformation, DLT）把投影合併為 11 個尺度固定係數：
$$
x=\frac{L_1X+L_2Y+L_3Z+L_4}{L_9X+L_{10}Y+L_{11}Z+1},\quad
y=\frac{L_5X+L_6Y+L_7Z+L_8}{L_9X+L_{10}Y+L_{11}Z+1}.
$$
交叉相乘，例如 $x=L_1X+L_2Y+L_3Z+L_4-xXL_9-xYL_{10}-xZL_{11}$，對 L 可線性初估。若令 Z＝0，就得到平面八係數形式；一般三維點則不能直接用平面 H 取代。[S05 pp.49–54；代數步驟補齊]

## 應用、限制與常見誤解
DLT 係數不同項有不同量綱，不能說全都無因次。由係數分解內外參，需處理尺度、正交性與相機約束；p.51–52 的較完整公式保留其出處，本頁不把簡單代入當完整穩定率定流程。[S05 pp.50–54]

## 來源與相關頁
[來源](../sources.md) · [空間旋轉](spatial-rotation.md) · [交會與方位](orientation-adjustment.md) · [工程案例](../cases/engineering-measurement.md)
