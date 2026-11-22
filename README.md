# 影像感測與 3D 場景重建 LLM Wiki

給自己複習課程的可追溯知識庫：保留公式推導、符號與應用案例，後續再以 Wiki 為來源製作初學者教學 HTML 簡報。

**目前：第 02 章「相機率定」試做，等待使用者確認整理方式。已 ingest 1／7 份課堂教材；尚未完成作業要求的至少 5 份 ingest，也尚未製作最終教學簡報。** 外部查核資料不拿來湊課堂教材匯入數。

## 閱讀入口
- [線上 HTML Wiki](https://holeinlove.github.io/3D-reconstruction-LLM-wiki/)：GitHub Pages 閱讀入口。
- [Wiki 首頁](wiki/index.md)：章節與概念雙入口。
- [第 02 章複習導覽](wiki/chapters/02-calibration.md)：建議從這裡開始。
- [HTML 閱讀入口](index.html)：下載／clone 專案後，直接雙擊 index.html；無須安裝，數學公式與搜尋可離線使用。GitHub 檔案頁只顯示原始碼，不是網頁預覽。
- [本次檢查紀錄](reports/pilot-02.md)、[疑點台帳](wiki/issues.md)、[流程設計](workflow/graph.md)。

## 專案文件
| 文件 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | AI 工作規則與驗收／停止條件 |
| [SKILL.md](SKILL.md) | 來源匯入與 Wiki 維護 SOP |
| [PRD.md](PRD.md) | 已確認需求、範圍與驗收 |
| [DESIGN.md](DESIGN.md) | 閱讀介面、公式、引用及頁面規範 |

## 重建與預覽
Python 3.10+ 與 Node.js，均只用標準函式庫；閱讀不需要這些工具。
```bash
python scripts/check.py
python scripts/build.py
node scripts/check_math.cjs
python -m http.server 8765
```
最後一個指令在專案根目錄執行，再開啟 http://localhost:8765 。Markdown 為唯一內容來源，修改後重建 HTML。版本固定的 markdown-it 與 KaTeX 位於 vendor/，授權見 [第三方說明](vendor/README.md)。

## GitHub 與公開網頁
儲存庫：https://github.com/holeinlove/3D-reconstruction-LLM-wiki

依使用者追加要求，GitHub Pages 已設定從 `main` 分支根目錄發布，公開入口為 https://holeinlove.github.io/3D-reconstruction-LLM-wiki/ 。`.nojekyll` 保留靜態檔案，後續推送 main 會觸發重新發布。部署結果可在 GitHub 的 Pages／Actions 查看。

## 來源與使用界線
課堂教材作者：詹鈞評，國立臺灣科技大學。原始 PPT 留在本機教材資料夾；儲存庫不含教材本體或投影片截圖。[來源索引](wiki/sources.md) 保存檔名、頁數、雜湊及引用定位。這些筆記為 AI 協助整理的課程複習成果，補充、算例與待查內容均另標示，不代表授課者核定內容。未替教材或第三方函式庫重新宣告授權。
