# 影像感測與 3D 場景重建 LLM Wiki

以七份課堂教材建立的個人複習知識庫，繁體中文加英文術語，保留關鍵公式推導、應用案例、來源頁碼與查核疑點。

**7／7 份教材已匯入，覆蓋 437 張投影片；已加入九個互動學習模組。** 已完成七章各自的教學 HTML 簡報（共 58 頁、九個互動示範），並保留原 22 頁課程總覽與作業流程。原始教材與實拍資料不在公開儲存庫，算例不冒充實測成果。

## 閱讀入口
- **[初學者教學 HTML 簡報](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/slides/)**：開啟即見七章卡片，點選進入該章簡報。
- [七章改版驗收](reports/chapters-check.md) · [課程總覽與作業流程](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/slides/overview.html)
- [初次簡報驗收紀錄](reports/slides-check.md)
- **[線上 Wiki](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/wiki.html)**
- **[互動學習實驗室](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/#p=labs%2Findex.md)**
- [Markdown 首頁](wiki/index.md)、[來源索引](wiki/sources.md)、[完整匯入紀錄](reports/course-import.md)。
- 下載／clone 專案後，直接開啟 [wiki.html](wiki.html) 可離線閱讀；公式、搜尋與互動資產都在本機。GitHub 的 HTML 原始碼頁不是網頁預覽。

## 互動模組
| 模組 | 能觀察的關係 |
| --- | --- |
| GSD／FOV | 距離、焦距、像元與物方範圍 |
| 徑向畸變 | 一階係數與網格彎曲 |
| 平面變換 | 相似／仿射／透視與退化條件 |
| 雙線性內插 | 四角權重與灰階值 |
| 比率測試／RANSAC | 候選歧義與抽樣次數 |
| MR／DR／CR | 計數分母、教材算例查核 |
| 旋轉／投影 | ω／φ／κ、矩陣與像點 |
| 極線 | 點到線、候選距離與共面約束 |
| 雙目深度 | 視差、基線與誤差放大 |

每個模組有單位、重設、即時結果、來源與模型限制；可用滑桿與鍵盤操作，不會上傳照片。

## 五份專案文件
[AGENTS.md](AGENTS.md)：AI 規則 · [SKILL.md](SKILL.md)：匯入 SOP · [PRD.md](PRD.md)：需求與驗收 · [DESIGN.md](DESIGN.md)：閱讀與互動規範。

## 建置與檢查
Python 3.10+、Node.js，只使用標準函式庫與專案內已固定版本資產；閱讀不需安裝工具。
```bash
python scripts/check.py
python scripts/build.py
python scripts/build_slides.py
node scripts/check_slides.cjs
node scripts/check_math.cjs
node scripts/check_labs.cjs
python -m http.server 8765
```
Markdown 是內容來源，修改後重建 HTML；不要只改 index.html 裡的內嵌資料。GitHub Pages 從 main 根目錄發布，推送後等待 Pages 工作完成。第三方資產與授權見 [vendor 說明](vendor/README.md)。

## 來源與版本
課堂教材作者：詹鈞評，國立臺灣科技大學。原始 PPT 留在本機教材資料夾；公開庫不含原始 PPT、逐頁截圖、完整擷取文字或個人絕對路徑。[catalog.json](sources/catalog.json) 保存來源指紋，[coverage.json](sources/coverage.json) 保存逐頁去向。

本次分三批整理，版本與檢查紀錄見 [course-import.md](reports/course-import.md)。AI 整理筆記不代表授課者已核定，疑點保持可見，外部查核與補充推導分列。結構／語法／理想算例檢查不能證明所有內容正確，也不等於實驗重現。

## 根網址入口
[根網址](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/) 直接呈現七章課程卡片。完整 Wiki 移至 wiki.html；舊根網址 #p= 來源連結會轉往 Wiki 對應頁，章節簡報來源亦直接指向新位置。
