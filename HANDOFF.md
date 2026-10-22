# 交接：北陸自駕 8 日 PWA

最後更新：2026-10-23

## 現況

- 線上網址：https://amyxpao.github.io/trip-2026/（GitHub Pages，`AmyxPao/trip-2026` 的 `main` 根目錄，公開 repo）
- 原始碼：本資料夾（本機 repo，origin 是 `AmyxPao/2026Kanazawa2.0`，**尚未 push**）
- 目前線上版本：Service Worker 快取版本 `hokuriku-v10`
- 產品脈絡：`PRODUCT.md`；視覺規格：`DESIGN.md`；設計方向紀錄：`.impeccable/surfaces/index-html.md`

## 已完成的功能

- 總覽（8 天，DAY 大字、今天朱色、出發倒數／旅途中「下一站」卡片附導航與撥電話）
- 單日時間軸：交通段與下一站旁有導航鈕、已過的站淡色、今日路線（Google Maps 多點，超過 5 點自動拆段）
- 單站面板：導航、撥電話、營業時間、備註、資料來源／參考來源
- 手機上編輯：每站所有欄位、新增／刪除（可復原）、拖曳與上下移排序、完成時檢查時刻順序；「改這一天的標題與住宿」（標題、住宿、注意、備案）
- 分帳：記一筆（常用 4 分類、付款／日期／分法收合、送出列固定）、總帳／分類／日期／分帳、刷卡 0.22 粗估→補帳單後反推同日同卡匯率、結清「済」章、刪帳可復原
- 雲端同步（只同步帳本）到使用者自己的 Google 試算表：`sync/ledger-sync.gs`（Apps Script）＋ `js/sync.js`；網址與密語只存在瀏覽器
- 清單：出發前清單、住宿、風險與季節、備份（匯出／匯入 .json）、匯出 Excel（6 張工作表）、還原成 Excel 版
- 離線（PWA）、深色模式、RWD（≥768px 左側分頁欄；≥1024px 單日與分帳兩欄）

## 使用者已做的決定（不要推翻）

- 總覽不放印章；**行程端完全沒有查證**：查證狀態與標籤已移除，查證結果併入備註，查證來源改稱「參考來源」（2026-10-22）
- 印章只留在分帳：我／伴（付款人）、估／実（匯率）、済（結清）
- 網頁取代 Excel；修改在手機上做；資料存手機＋備份檔
- 同步只同步帳本，維持「網址＋密語」做法（不改 Google 帳號登入）
- 住宿資訊公開在 GitHub Pages 沒關係
- 天數一律寫「DAY」

## 檔案結構

- `index.html`、`css/app.css`、`manifest.webmanifest`、`sw.js`、`fonts/`、`icons/`
- `js/app.js` 路由與事件；`js/store.js` 本機儲存與備份；`js/trip.js` 行程推算（下一站、導航目的地、時刻檢查、舊資料轉換 `normalizeStops`）
- `js/view-trip.js` 總覽／單日／單站／編輯；`js/view-ledger.js` 分帳；`js/view-misc.js` 地圖／清單
- `js/ledger.js` 換算與結算；`js/sync.js` 試算表同步；`js/xlsx.js`＋`js/export-xlsx.js` 匯出 Excel
- `data/trip.json` 初始行程；`data/maps/*.webp` 9 張靜態路線圖
- `tools/xlsx_to_json.py` 從 `北陸自駕行程.xlsx` 產生 `data/trip.json` 與地圖（只在重建初始資料時用）

## 部署方式（每次改完）

1. 本機 repo commit。
2. `sw.js` 的 `VERSION` 加 1（例如 `hokuriku-v11`），不然手機會一直用舊快取。
3. 把有改的檔案複製到 `trip-2026` 的工作副本（`gh repo clone AmyxPao/trip-2026`），commit、push 到 `main`。
4. 等 Pages 建置：`gh api repos/AmyxPao/trip-2026/pages/builds/latest`。
5. 手機打開會提示「有新版本」，關掉再開就更新。使用者在手機上改的行程與帳不會被蓋掉。

## 還沒做／待決定

- 互動地圖（可縮放、離線底圖，建議 PMTiles）：使用者有興趣，尚未規劃，從 `/dev-ui-impeccable shape 地圖頁` 開始
- 評論的次要觀察（未處理）：電腦版頁首沒貼齊左右、清單頁「電話確認」號碼不能點撥、旅途中地圖頁沒先顯示今天的圖
- `.impeccable/surfaces/index-html.md` 的 Direction contract 仍寫著「查證過的站蓋上印泥章」等舊描述，需改寫
- 可選：設定裡加「產生隨機密語」按鈕（使用者暫不要）
- 分帳印章顏色：「我」與舊的「衝突」同色、「伴」與「次級來源」同色；查證已移除，這個衝突已不存在

## 測試方式

- 本機：`python -m http.server 8765`，用瀏覽器開 http://127.0.0.1:8765/
- 自動截圖腳本放在 Claude 的暫存資料夾（不在 repo），之後需要可重寫：headless Edge＋CDP，可模擬「旅途中某時刻」與注入範例帳本
- 設計檢查：`impeccable detect --json index.html css/app.css js`，目前 0 個問題
- 最近一次評論分數：28/40（2026-10-22），5 個優先問題已修，可再跑 `/dev-ui-impeccable critique index.html` 看分數

## 注意事項

- `北陸自駕行程.xlsx` 只在本機 repo，不放網站
- `localStorage` 鍵：`hokuriku-trip-v1`（行程＋帳本）、`hokuriku-sync-v1`（同步網址與密語）
- Excel 匯出不能匯回；換手機要用 .json 備份
- 同步程式 `sync/ledger-sync.gs` 的 `SECRET` 由使用者自己改，網站上公開的版本是預設文字
