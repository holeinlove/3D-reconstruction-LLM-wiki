from pathlib import Path
import json,copy
base=json.loads(Path('slides/deck.json').read_text(encoding='utf-8'))['slides']
chapters=[]
def slide(t,b,p,label,lab=None,note=''):
 return dict(title=t,body=b,refs=[dict(path=p,label=label)],lab=lab,note=note,kind='lesson')
def old(n):return copy.deepcopy(base[n-1])
def make(num,title,desc,items,chapter):
 cover=slide(title,fr'<p class="lead">{desc}</p><div class="journey"><span>理解概念</span><b>→</b><span>操作觀察</span><b>→</b><span>回顧應用</span></div><p>第 {num:02d} 章 · 初學者教學與複習<br>使用下方箭頭翻頁，隨時回到章節首頁。</p>',chapter,f'S{num:02d}：章節導覽與教材頁碼')
 end=slide('本章回顧：用自己的話說一次',fr'<p>{desc}</p><p class="callout">回想本章：關鍵公式需要哪些條件？互動參數改變後，你能解釋結果嗎？</p><p>需要完整推導時，展開下方「來源與延伸」。</p><p><a href="index.html">← 回到七章課程</a></p>',chapter,f'S{num:02d}：完整筆記與延伸')
 d=dict(title=title,description=desc,chapter=num,language='zh-Hant',slides=[cover]+items+[end]);chapters.append(d)
make(1,'影像感測器','先理解影像品質，再看像素、焦距與距離如何決定取樣範圍。',[
 slide('相機記錄了什麼？',r'<p>影像感測器（Image Sensor）把光轉成電訊號，再形成數位影像。CCD／CMOS 是感測技術；RGB、熱紅外與多光譜則關心不同成像資訊。</p><p class="callout">像素更多，不代表重建一定更準。先檢查清晰度、曝光與可辨識紋理。</p>','wiki/concepts/sensing-quality.md','S01 pp.2–11,12–38'),
 slide('解析度不只一種',r'<div class="split"><div><h3>空間與波譜</h3><p>空間取樣：每像素涵蓋多大範圍？波譜：能分辨哪些波段？</p></div><div><h3>輻射與時間</h3><p>輻射：灰階數位化層級。時間：多久能再次觀測？</p></div></div><p>n bit 可表示 $2^n$ 階；2 bit 是 4 階、0–3。教材原頁差異已列疑點。</p>','wiki/concepts/sensing-quality.md','S01 pp.12–28；Wiki 算術核對'),
 slide('曝光是一種取捨',r'<p>光圈值 N＝f/D；固定場景與透過率時，相對曝光量與 t/N² 成正比。</p><p>把曝光時間拉長可增加進光量，也可能讓移動物體模糊；過曝遺失的資訊不能靠亮度映射恢復。</p><p class="callout">先確保你要匹配的細節真的被拍下來。</p>','wiki/concepts/sensing-quality.md','S01 pp.29–42；比例式為 Wiki 補充'),old(5),old(6),
 slide('HW1：從任務反推取像參數',r'<div class="journey"><span>目標大小</span><b>→</b><span>所需 GSD</span><b>→</b><span>焦距／距離</span><b>→</b><span>試拍檢查</span></div><p>先決定要辨識多小的細節，再選視野與取樣範圍；同時檢查曝光、重疊與相機選擇。</p><p>這裡整理作業方法，沒有宣稱已完成新的拍攝實驗。</p>','wiki/cases/hw1-camera.md','S01 pp.93–104：HW1 與取像案例')], 'wiki/chapters/01-sensors.md')
make(2,'相機率定','學會分辨內參、外參與畸變，知道率定參數如何取得及檢查。',[
 old(4),old(7),
 slide('從相機方向換成像素',r'<p>採 CV 前方虛擬像平面、忽略 skew 時：</p><div class="equation">$$u=f_x X_c/Z_c+c_x,\qquad v=f_y Y_c/Z_c+c_y$$</div><p>fₓ、fᵧ 是 pixel 單位焦距；cₓ、cᵧ 是主點。實體焦距 f（mm）要除以像元尺寸（mm/pixel），才變成像素焦距。</p><p class="callout">PM 與 CV 的軸向和像平面約定不同，不能只換數值而不換符號。</p>','wiki/concepts/intrinsics.md','S02 pp.12–19：內參與座標'),old(8),
 slide('棋盤格怎麼幫忙率定？',r'<div class="journey"><span>已知格長</span><b>→</b><span>多角度拍攝</span><b>→</b><span>角點對應</span><b>→</b><span>估參數</span></div><p>平面點取 Z＝0，可得到 H ∼ K[r₁ r₂ t]。多種姿態提供不同約束，再估畸變並精化重投影誤差。</p><p>教材建議至少 10 張以上、涵蓋旋轉與傾斜；不是隨便拍 10 張就保證成功。上述矩陣關係為 Wiki 依 Zhang 補充推導。</p>','wiki/concepts/checkerboard.md','S02 pp.35–36；E03 §2.2–3.3'),
 slide('小殘差，不是唯一驗收標準',r'<p>重投影誤差：將已知物點投回影像，比較預測像點與觀測像點。</p><p>需說明 RMSE 是每點二維距離、每座標分量，或自由度校正尺度；分母不同，數字不能直接比較。</p><p class="callout">還要檢查影像覆蓋、角點品質、參數穩定性與新影像表現。修正影像與重新率定是不同工作。</p>','wiki/concepts/checkerboard.md','S02 pp.35–44；Wiki RMSE 定義與自建算例')], 'wiki/chapters/02-calibration.md')
make(3,'平面影像轉換','比較相似、仿射與透視模型，再理解估參數與像素內插。',[
 old(11),
 slide('模型多一點彈性，代表什麼？',r'<table><tr><th>模型</th><th>自由度</th><th>能描述</th></tr><tr><td>相似 Similarity</td><td>4</td><td>平移、旋轉、共同尺度</td></tr><tr><td>仿射 Affine</td><td>6</td><td>再加入非等向尺度與剪切</td></tr><tr><td>透視 Homography</td><td>8</td><td>平面透視效果</td></tr></table><p>非退化配置下，理論最少對應點分別為 2、3、4；實作仍需更多可靠點與檢查。</p>','wiki/concepts/planar-transforms.md','S03 pp.3–18'),
 slide('動手試：同一矩形，三種模型',r'<p>先從相似切到仿射，再切到透視。觀察角度、平行線與矩陣 H；跨越投影無窮遠時會提示退化。</p>','wiki/concepts/planar-transforms.md','S03 pp.7–18','planar'),
 slide('最小二乘：讓所有點一起說話',r'<p>選好模型後，利用多組對應點估參數。固定 v＝Aθ−L，讓殘差平方和最小：</p><div class="equation">$$J=v^Tv,\qquad A^TA\hat\theta=A^TL$$</div><p>θ：模型參數；A：設計矩陣；L：觀測。需要足夠秩與良好幾何配置；實作用 QR／SVD 比直接求反矩陣更合適。</p>','wiki/concepts/least-squares.md','S03 pp.27–32；Wiki 符號整理與實作補充'),
 slide('變換位置後，像素值從哪來？',r'<p>反算（Inverse Mapping）：逐一走訪輸出像素，找回輸入影像的座標；落在非整數位置時，需要內插。</p><p>最鄰近取一點；雙線性取四角加權；它們不會創造原圖沒有的真實細節。</p>','wiki/concepts/interpolation.md','S03 pp.35–54'),
 slide('動手試：四角灰階怎麼混合？',r'<p>中心點的四個權重各是 1/4。移到角落時，該角權重會變成 1；看看結果是否符合預測。</p>','wiki/concepts/interpolation.md','S03 pp.47–48','bilinear'),
 slide('HW3：拼得上，還要看誤差',r'<p>比較不同模型的拼接結果與誤差向量；檢查周邊是否出現系統性偏差，並使用未參與估計的點評估。</p><p class="callout">更多參數可能降低擬合殘差，卻不一定提高新點精度。</p>','wiki/cases/hw3-stitching.md','S03 pp.19–34：拼接與模型比較')], 'wiki/chapters/03-planar.md')
make(4,'影像匹配','分清楚偵測、描述、配對與幾何驗證，理解匹配如何接到重建。',[
 old(9),
 slide('哪種位置容易被重新找到？',r'<div class="split"><div><h3>平坦區與邊緣</h3><p>平坦區往哪移都相似；邊緣沿著線移動也可能很像。</p></div><div><h3>角點 Corner</h3><p>往兩個方向移動都改變外觀，較有機會被明確定位。</p></div></div><p>Harris 以窗口灰階變化形成矩陣 M，再用 R＝det(M)−k·tr(M)² 判斷；不是偵測到角點就已完成匹配。</p>','wiki/concepts/feature-detection.md','S04 pp.3–11'),
 slide('偵測器與描述子，工作不同',r'<p>FAST、DoG 等方法決定在哪裡取特徵；描述子則表示附近外觀，供跨影像比較。</p><p>區域匹配可用正規化互相關（NCC）比較；描述子匹配則依其形式使用適合的距離。</p><p class="callout">亮度、尺度、視角與重複紋理都可能影響配對；不要把所有方法視為相同角點公式。</p>','wiki/concepts/feature-matching.md','S04 pp.33–48；偵測器見 pp.12–20'),old(10),
 slide('RANSAC：先問模型是否適合',r'<p>反覆抽少量候選 → 估模型 → 檢查支持該模型的內點 → 保留共識較好的結果，再重估。</p><p>平面可考慮 H；一般雙視圖可考慮 F。門檻單位、模型選擇及退化配置都需要檢查。</p><p class="callout">找到很多內點，仍不等於三維座標或絕對尺度已知。</p>','wiki/concepts/robust-estimation.md','S04 pp.49–50'),old(16)],'wiki/chapters/04-matching.md')
make(5,'空間轉換與共線條件式','理解座標旋轉、物點投影及交會，連到實際工程量測。',[
 slide('同一個點，在兩套座標裡',r'<p>外方位描述相機位置與姿態。計算前先說明：矩陣把哪個空間轉到哪個空間？是旋轉物點，還是旋轉座標軸？</p><p>本章互動採課堂 PM 慣例：M＝Mκ Mφ Mω。旋轉順序改變，結果一般也會改變。</p>','wiki/concepts/spatial-rotation.md','S05 pp.3–15；旋轉符號疑點另列'),
 slide('動手試：轉相機，像點往哪移？',r'<p>先只改 κ，再加入 ω、φ。觀察矩陣、像點與可見性提示；此模組採 PM 約定，像方結果單位為 mm。</p>','wiki/concepts/spatial-rotation.md','S05 pp.6–13,18–24','rotation'),
 slide('共線條件：三個點在一條線上',r'<p>理想像點、攝影中心與物點共線。令 q＝M(A−O)，在課堂 PM、無畸變模型中：</p><div class="equation">$$x_a-x_p=-f q_1/q_3,\qquad y_a-y_p=-f q_2/q_3$$</div><p>由像向量 λq 的第三列 −f＝λq₃，消去 λ，得到上式。q₃＝0 時沒有有限投影；還須檢查點在相機前方。</p>','wiki/concepts/collinearity.md','S05 pp.16–24；Wiki 推導補齊'),
 slide('前方交會與後方交會',r'<div class="split"><div><h3>前方交會</h3><p>相機關係已知，由多幅影像中的對應射線估物點。</p></div><div><h3>後方交會</h3><p>物方控制點已知，由其像點估相機姿態。</p></div></div><p>光束法平差同時調整相機與三維點；方程數足夠仍不保證幾何非退化或解唯一。</p>','wiki/concepts/orientation-adjustment.md','S05 pp.25–28,55–61'),
 slide('DLT 如何連回平面模型？',r'<p>直接線性轉換（DLT）以分式描述三維點到影像的投影，交叉相乘後可對係數做線性初估。</p><p>把物點限制在 Z＝0 的平面，就能化成平面八係數形式；一般三維場景不能直接用平面 H 取代。</p>','wiki/concepts/collinearity.md','S05 pp.49–54'),
 slide('案例：量到板子動，還是相機動？',r'<p>教材以雙相機量測太陽能板變形：同步拍攝 → 偵測標點 → 前方交會 → 必要的晃動修正 → 比較不同時間的三維位置。</p><p class="callout">先固定比較座標系；未補償的相機移動可能被誤當成板體變形。</p><p>水下案例另須考慮折射與率定環境。本 Wiki 未重現實測精度。</p>','wiki/cases/engineering-measurement.md','S05 pp.29–48')],'wiki/chapters/05-collinearity.md')
make(6,'影像匹配之應用','從多光譜與地理對位案例，學會選模型並看懂匹配指標。',[
 slide('不同波段，看見的外觀可能不同',r'<p>RGB、近紅外與熱影像對同一場景可能呈現不同灰階關係；多鏡頭還有不同姿態與畸變。</p><p>影像套合（Registration）希望讓不同來源的像素對應同一物點，不只是把兩張圖疊在一起。</p>','wiki/concepts/multispectral-registration.md','S06 pp.4–10'),
 slide('點數要控制，幾何也要驗證',r'<p>教材的 N-SURF 思路分尺度找局部極值，再用累積分布（CDF）選門檻，控制各影像的特徵數。</p><p>比較仿射 AT、透視 PT 與附加畸變項的 EPT 時，要看殘差向量是否仍有系統模式。</p><p class="callout">某案例有效的模型，不代表所有場景都最好。</p>','wiki/concepts/multispectral-registration.md','S06 pp.11–15,24–29'),
 slide('三個比率，三種分母',r'<p>依教材定義：FA、FB 為特徵數，M 為匹配對，D 為重複匹配，CM 為過濾後正確數。</p><div class="equation">$$MR=100\frac{2M}{F_A+F_B},\quad DR=100\frac{D}{M},\quad CR=100\frac{CM}{M-D}$$</div><p>名稱與分母需隨研究確認；分母為零是未定義，不是 0%。</p>','wiki/concepts/matching-metrics.md','S06 pp.16–18'),
 slide('動手試：改計數，看看指標',r'<p>用教材 FA＝13、FB＝15、M＝6、D＝2、CM＝3 重算。MR 應為 42.86%，原頁 66% 已列疑點；DR 約 33.33%，CR 為 75%。</p>','wiki/concepts/matching-metrics.md','S06 p.16；Wiki 算術核對','metrics'),
 slide('案例：UAV 對位衛星影像',r'<p>將空拍影像與具有地理參考的影像建立對應，再進行幾何驗證與位置估計。</p><p>要一起報告成功／失敗數、像方誤差與物方位置誤差；教材不同計數的分母疑點不能自行補成成功率。</p>','wiki/cases/geographic-registration.md','S06 pp.34–42,59–68'),
 slide('學習式匹配也有不同角色',r'<p>SuperPoint 處理特徵偵測與描述；SuperGlue 結合特徵資訊推斷匹配；LightGlue 是另一種具有適應性計算的匹配方法。</p><p class="callout">教材標題與架構圖有名稱差異，已在 Wiki 查核區分。學習式方法仍需幾何與場景驗證。</p>','wiki/concepts/learned-matching.md','S06 pp.43–58；E06／E07 外部查核')],'wiki/chapters/06-applications.md')
make(7,'核幾何與立體視覺','由點到極線的限制，推進到視差、深度與點雲。',[
 old(12),old(13),
 slide('F 與 E：相同幾何，不同座標',r'<p>F 作用在齊次像素座標；本質矩陣 E 作用在正規化射線。已知內參時：</p><div class="equation">$$E=K\prime{}^T F K=[t]_\times R$$</div><p>分解 E 可得旋轉和平移方向的候選，再用點是否位於兩相機前方選解。影像本身不會自動給出公尺尺度。</p>','wiki/concepts/essential-decomposition.md','S07 pp.24–32；Wiki 對不同 K 的補充'),old(14),old(15),
 slide('從視差圖到點雲',r'<div class="journey"><span>影像糾正</span><b>→</b><span>匹配代價</span><b>→</b><span>代價聚合</span><b>→</b><span>視差／點雲</span></div><p>SGM／SGBM 在匹配代價與視差平滑間取捨。無紋理、重複圖案、遮蔽與深度邊界都可能失敗。</p><p class="callout">必須保留無效視差遮罩，不把所有像素硬轉成可信三維點。</p>','wiki/concepts/stereo-matching.md','S07 pp.51–54；E08 實作補充'),old(17)],'wiki/chapters/07-epipolar.md')
Path('slides/chapters').mkdir(exist_ok=True)
for d in chapters:Path(f'slides/chapters/{d["chapter"]:02d}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print([(d['chapter'],len(d['slides'])) for d in chapters])
