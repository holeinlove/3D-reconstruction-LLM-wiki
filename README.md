# 影像感測與 3D 場景重建 LLM Wiki

以七份課堂教材建立的個人複習知識庫，繁體中文加英文術語，保留關鍵公式推導、應用案例、來源頁碼與查核疑點。

**7／7 份教材已匯入，覆蓋 437 張投影片；已加入九個互動學習模組。** 已完成七章各自的教學 HTML 簡報（共 58 頁、九個互動示範），並保留原 22 頁課程總覽與作業流程。原始教材與實拍資料不在公開儲存庫，算例不冒充實測成果。

## 作業繳交內容：老師要求的六個項目

想看教學成果，先開啟 **[七章教學簡報首頁](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/)**；想確認資料整理與製作過程，依照下表閱讀。

| 老師要求的項目 | 請看這裡 | 這份資料在說什麼？ |
| --- | --- | --- |
| **1. LLM Wiki 主題與簡短介紹** | 本頁最上方的「影像感測與 3D 場景重建 LLM Wiki」介紹 | 說明主題、複習用途、七份教材與整理成果。 |
| **2. LLM Wiki 連結或成果** | [開啟完整 Wiki](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/wiki.html) · [GitHub 專案](https://github.com/holeinlove/3D-reconstruction-LLM-wiki) | Wiki 是整理好的知識庫，保留公式推導、案例和來源頁碼；GitHub 保存 Markdown、程式與專案文件。 |
| **3. 教學 HTML 簡報連結** | [開啟七章教學簡報](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/) | 先選第 01～07 章，再翻頁學習；七章共 58 頁，包含九個互動示範。 |
| **4. Loop／Graph 流程圖或文字說明** | [查看完整製作流程](workflow/graph.md) · [翻頁版流程說明](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/slides/overview.html#s18) | 說明資料怎麼取得、核對、整理成 Wiki，再產生簡報；出錯時回到哪個步驟重做，以及停止條件。 |
| **5. 一次實際執行的結果或檢查紀錄** | [Wiki 資料整理與檢查紀錄](reports/course-import.md) · [目前七章簡報的檢查紀錄](reports/chapters-check.md) | 前者記錄三批教材匯入與查核；後者記錄七章卡片、58 頁桌面／手機、九個互動及根網址驗收。 |
| **6. 反思與檢查流程調整** | [內容整理的反思](reports/course-import.md) · [七章介面與流程的反思](reports/chapters-check.md) · [翻頁版反思](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/slides/overview.html#s21) | 閱讀報告中的「反思」段落：跨章符號、單位與適用條件容易失真，因此把檢查提前；介面則改成先選章再學習。沒有節點失敗次數統計，不宣稱哪個節點有統計上的最高錯誤率。 |

### 其他連結：補充資料與歷史紀錄

以下是協助操作或查證的補充，不是另外增加的繳交項目。

| 連結 | 用途 | 對應作業項目 |
| --- | --- | --- |
| [互動學習實驗室](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/wiki.html#p=labs%2Findex.md) | 集中操作九個模型；各章簡報也已內嵌對應示範。 | 第 2、3 項的補充成果 |
| [Markdown 知識庫首頁](wiki/index.md) · [來源索引](wiki/sources.md) | 查看筆記原始檔，確認每份教材的代號與引用方式。 | 第 2 項；支援第 5 項查證 |
| [22 頁課程總覽與作業流程](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/slides/overview.html) | 原本的入門總覽，後半部包含製作流程、檢查與反思。 | 第 3、4、5、6 項的補充 |
| [初次簡報檢查紀錄](reports/slides-check.md) · [簡化介面檢查紀錄](reports/interface-check.md) | 保存前兩版實作發現的問題與修正，不當成目前七章版的最新驗收。 | 第 5、6 項的歷史佐證 |

**離線閱讀：**下載整個專案後，開啟 `index.html` 看七章首頁，或開啟 `wiki.html` 看完整 Wiki。線上閱讀直接使用上表的網頁連結；GitHub 顯示 HTML 原始碼的頁面不是簡報預覽。

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
Markdown 是內容來源，修改後重建 HTML；不要只改 wiki.html 裡的內嵌資料。GitHub Pages 從 main 根目錄發布，推送後等待 Pages 工作完成。第三方資產與授權見 [vendor 說明](vendor/README.md)。

## 來源與版本
課堂教材作者：詹鈞評，國立臺灣科技大學。原始 PPT 留在本機教材資料夾；公開庫不含原始 PPT、逐頁截圖、完整擷取文字或個人絕對路徑。[catalog.json](sources/catalog.json) 保存來源指紋，[coverage.json](sources/coverage.json) 保存逐頁去向。

本次分三批整理，版本與檢查紀錄見 [course-import.md](reports/course-import.md)。AI 整理筆記不代表授課者已核定，疑點保持可見，外部查核與補充推導分列。結構／語法／理想算例檢查不能證明所有內容正確，也不等於實驗重現。

## 根網址入口
[根網址](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/) 直接呈現七章課程卡片。完整 Wiki 移至 wiki.html；舊根網址 #p= 來源連結會轉往 Wiki 對應頁，章節簡報來源亦直接指向新位置。
