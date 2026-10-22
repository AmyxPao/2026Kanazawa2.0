---
name: 北陸自駕 8 日
description: 一本スタンプ帳風格的離線可用的北陸自駕行程與兩方分帳 PWA
colors:
  paper: "#f3f5f7"
  sheet: "#ffffff"
  ink: "#17213b"
  ink-2: "#445070"
  ink-3: "#5e6984"
  rule: "#dce1e9"
  rule-strong: "#c4cbd8"
  navy: "#1d2f5e"
  navy-2: "#2a4280"
  on-navy: "#ffffff"
  on-navy-2: "#c9d3ec"
  shu: "#c8321f"
  shu-wash: "#fbe9e6"
  ink-sec: "#a26f08"
  ink-call: "#6d3f94"
  ink-bad: "#24407a"
  ink-na: "#8a93a8"
  danger: "#b3261e"
  focus: "#2a4280"
  paper-dark: "#0f1524"
  sheet-dark: "#161e31"
  ink-dark: "#e8ecf5"
  ink-3-dark: "#96a0b8"
  rule-dark: "#26304a"
typography:
  display:
    fontFamily: "Barlow Condensed, Arial Narrow, Noto Sans TC, PingFang TC, Microsoft JhengHei, system-ui, sans-serif"
    fontSize: "76px"
    fontWeight: 700
    lineHeight: 0.8
    letterSpacing: "-0.01em"
    fontFeature: "tnum"
  headline:
    fontFamily: "Barlow Condensed, Arial Narrow, Noto Sans TC, PingFang TC, Microsoft JhengHei, system-ui, sans-serif"
    fontSize: "52px"
    fontWeight: 700
    lineHeight: 0.86
    letterSpacing: "0.01em"
    fontFeature: "tnum"
  numeral:
    fontFamily: "Barlow Condensed, Arial Narrow, Noto Sans TC, PingFang TC, Microsoft JhengHei, system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "0.01em"
    fontFeature: "tnum"
  display-lg:
    fontFamily: "Barlow Condensed, Arial Narrow, Noto Sans TC, PingFang TC, Microsoft JhengHei, system-ui, sans-serif"
    fontSize: "92px"
    fontWeight: 700
    lineHeight: 0.8
    fontFeature: "tnum"
  numeral-lg:
    fontFamily: "Barlow Condensed, Arial Narrow, Noto Sans TC, PingFang TC, Microsoft JhengHei, system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 700
    lineHeight: 1.1
    fontFeature: "tnum"
  numeral-sm:
    fontFamily: "Barlow Condensed, Arial Narrow, Noto Sans TC, PingFang TC, Microsoft JhengHei, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 600
    lineHeight: 1.2
    fontFeature: "tnum"
  title-lg:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 800
    lineHeight: 1.3
  title:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 800
    lineHeight: 1.35
  lead:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 700
    lineHeight: 1.4
  input:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1.45
  label-tab:
    fontFamily: "Noto Sans TC, PingFang TC, Hiragino Sans, Microsoft JhengHei, Yu Gothic UI, system-ui, sans-serif"
    fontSize: "11.5px"
    fontWeight: 700
  seal:
    fontFamily: "Seal, Noto Sans TC, sans-serif"
    fontSize: "19px"
    fontWeight: 400
rounded:
  tag: "4px"
  field: "10px"
  control: "12px"
  sheet: "18px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  gutter: "16px"
  lg: "22px"
components:
  button:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 18px"
    height: "46px"
  button-primary:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.control}"
    padding: "0 18px"
    height: "46px"
  button-danger:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.danger}"
    rounded: "{rounded.control}"
    padding: "0 18px"
    height: "46px"
  button-danger-armed:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.control}"
  chip:
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0 14px"
    height: "42px"
  chip-selected:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.pill}"
  input:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "10px 12px"
    height: "46px"
  segment:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.field}"
    height: "40px"
  segment-selected:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.field}"
  tabbar:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink-3}"
    typography: "{typography.label-tab}"
    height: "64px"
  tabbar-active:
    textColor: "{colors.navy}"
  masthead:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    padding: "28px 16px 22px"
  fab:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.pill}"
    padding: "0 22px 0 18px"
    height: "54px"
  sheet:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sheet}"
    padding: "8px 16px 20px"
  stamp:
    textColor: "{colors.shu}"
    typography: "{typography.seal}"
    size: "34px"
---

# Design System: 北陸自駕 8 日

## Overview

**Creative North Star: "The Stamp Book（スタンプ帳）"**

整個介面是一本車站／道之驛的蓋章本：冷白厚卡紙、海軍藍的書脊。印章只留在分帳：誰付的「我／伴」、匯率「估／実」、結清的「済」，蓋章的動作就是帳目狀態改變的回饋。行程本身不蓋章（原本的查證結果已併入備註，不再顯示查證狀態）。除了印章之外，頁面幾乎沒有裝飾，層級完全由「巨大的數字」對比「小而密的中文」撐起：日數、倒數、時間、金額都是 Barlow Condensed 的窄體大數字，中文內容則是系統黑體。

密度偏高、單欄、為單手在戶外冬季光線下操作而設計。頂部是一條深海軍藍的導覽列，內容區是卡紙底色上用 1px 髮線分隔的列表，而不是一張張浮起的白卡片；只有浮在內容之上的東西（底部面板、新增按鈕、提示）才有陰影。深色模式把卡紙換成深藍黑、印泥提亮，印章改為一般混合以免在深底上消失。

已確認拒絕的方向：旅遊 App 常見的白卡片牆與日期膠囊分頁。

**Key Characteristics:**
- 四色印泥章（雙圈＋單一印字、略帶油墨毛邊與傾斜）是唯一的狀態語言
- 朱色同時代表「官方確認」與「今天／下一站」，全畫面只有這一個暖色焦點
- 窄體大數字（Barlow Condensed）負責層級，中文黑體負責內容
- 髮線分隔的平面列表，陰影只給浮層
- 海軍藍是唯一的結構色：頂列、主要按鈕、選取狀態
- 單欄最寬 560px，底部固定五分頁

## Colors

冷灰白卡紙、深海軍藍骨架，加上四色印泥：整體偏冷，只有朱色是暖的。

### Primary
- **海軍藍封面（Navy Cover）**（#1d2f5e）：頂部導覽列與總覽頂區的底色、主要按鈕、選取中的膠囊與分段按鈕、底部分頁的目前頁、支出長條圖，也是 PWA 的 `theme-color`。淺色模式下日數大字也用它。
- **深一階海軍藍（Navy Deep Link）**（#2a4280）：文字連結、輸入游標、焦點外框；深色模式下改當主要按鈕與 FAB 的底色。

### Secondary
- **朱印泥（Shu Vermilion）**（#c8321f）：「官方確認」章（`--ink-ok` 與它同值）、已結清的「済」章、今天那一列的日數、下一站的時間、時間軸上的「今天」字樣、重點站的星形圖示。
- **朱暈（Shu Wash）**（#fbe9e6）：只用在時間軸上「下一站」那一列的底色。

### Tertiary
- **黃土印泥（Ochre Ink）**（#a26f08）：「次級來源」章與「估」（粗估匯率）章；旅伴「伴」章也沿用此色（`--ink-mate`）。方向合約原寫 #b07a0e，實作為了在卡紙上達到對比度而壓暗到 #a26f08，以實作為準。
- **紫印泥（Violet Ink）**（#6d3f94）：「需電話確認」章「電」。
- **靛藍印泥（Indigo Ink）**（#24407a）：「有衝突」章「衝」；本人「我」章與「実」（實際匯率）章也沿用此色（`--ink-me`）。
- **褪色印泥（Faded Ink）**（#8a93a8）：「不需查」的文字標籤色。

### Neutral
- **冷白卡紙（Card Stock）**（#f3f5f7）：頁面底色，也是輸入框與重新指派區塊的底色（比面板再低一階）。
- **白頁（Sheet White）**（#ffffff）：底部面板、按鈕、提示條、結算區、底部分頁（94% 不透明加模糊）。
- **墨（Ink）**（#17213b）：主要文字；提示（toast）以它為底、卡紙色為字。
- **淡墨（Ink 2）**（#445070）：次要文字、日期、備註、未選取分段。
- **灰墨（Ink 3）**（#5e6984）：說明文字、欄位標題、未選取分頁、圖示。
- **髮線（Hairline）**（#dce1e9）：列與列之間的 1px 分隔線、長條圖軌道。
- **粗髮線（Strong Hairline）**（#c4cbd8）：按鈕與輸入框的外框、虛線、面板把手、箭頭。
- **藍底白字（On Navy）**（#ffffff）／**藍底淡字（On Navy 2）**（#c9d3ec）：海軍藍頂列上的主文字與副文字。
- **警示紅（Danger）**（#b3261e）：刪除按鈕、表單錯誤；刻意與朱印泥分開，避免「確認」和「危險」混為一色。

### Named Rules
**The One Vermilion Rule.** 朱色只代表兩件事：「官方確認／已結清」和「今天／下一站」。它不當按鈕色、不當裝飾、不當警示；危險動作一律用 Danger 紅。

**The Ink Pad Rule.** 印章只用在分帳：付款人「我」（靛藍）／「伴」（黃土）、匯率「估」（黃土）／「実」（靛藍）、結清「済」（朱）。行程端沒有任何查證狀態或標籤；原本的查證結果已併進每站的「備註」。

**The Navy Spine Rule.** 海軍藍是唯一的結構與互動色；選取、主要動作、目前位置都用它，不另引入第二個品牌色。

## Typography

**Display Font:** Barlow Condensed 600／700（自架 woff2，備援 Arial Narrow，再退到中文黑體）
**Body Font:** 系統中文黑體（Noto Sans TC、PingFang TC、Hiragino Sans、Microsoft JhengHei、Yu Gothic UI、system-ui）
**Label/Mono Font:** Seal（Yuji Syuku 子集，只含「確 次 電 衝 済 実 估 我 伴 未」10 字，`font-display: block`）

**Character:** 窄體運動風數字像車票與里程表，負責「多少、幾點、第幾天」；黑體 700–800 粗字負責地名與動作；毛筆印字只活在印章裡。所有數字都套 `tabular-nums`。

### Hierarchy
字級全部走 CSS token，不寫死數值：中文 `--fs-micro` 11.5／`--fs-label` 13／`--fs-small` 14／`--fs-body` 15／`--fs-lead` 17／`--fs-title` 22／`--fs-title-lg` 28（768px 以上的頁首）；數字 `--fn-sm` 17／`--fn-md` 21／`--fn-lg` 30／`--fn-headline` 52／`--fn-display` 76／`--fn-display-lg` 92（768px 以上的倒數）。輸入框固定 `--fs-input` 16px，避免 iOS 聚焦時自動放大。
- **Display**（Barlow 700，76px，行高 0.8）：總覽頂區的出發倒數天數。
- **Headline**（Barlow 700，52px，行高 0.86）：8 天列表左側的日數；結算金額用同一角色放到 56px（行高 1）。
- **Numeral**（Barlow 600，21px，行高 1.1）：時間軸的時刻。同族的 16–22px 用於日期、明細金額與總計，合計放到 30px，金額輸入框 34px／700。
- **Title**（黑體 800，22px，行高 1.35）：單日標題；面板標題 21px、總覽 h1 24px、區塊標題 19px、頂列標題 17px。
- **Body**（黑體 400，15px，行高 1.55）：內文；站名與日主軸為 16px／700；備註與中繼資訊 12.5–14px。長說明（查證內容、註記）行高放寬到 1.6–1.65。
- **Label**（黑體 700，13px）：表單欄位標題、日期群組標題（800）；分頁標籤 11.5px／700。

### Named Rules
**The Big Number Rule.** 層級由數字撐起：日數、倒數、時刻、金額一律用 Barlow Condensed 放大；中文標題最大 24px，不跟數字搶。

**The Seal-Only Face Rule.** Seal 字型只能出現在印章 SVG 內。新增印字必須重新子集化字型檔，否則會退回黑體。

## Layout

單欄手機版面，內容區最寬 560px 置中，左右留白固定 16px（`--gutter`）。底部固定五分頁（總覽、今天、地圖、分帳、清單）高 64px 加 safe-area，內容底部預留同等空間再加 24px；寬度 600px 以上時分頁列也限寬 560px 並加左右髮線。次頁頂列 sticky、最小高 52px，左 44px 返回鍵、中標題、右膠囊動作鈕；分帳的四格分段控制也 sticky 貼在頂端。

列表是對齊欄位的格線：8 天列為「58px 日數（上方小字 DAY）｜內容｜18px 箭頭」，時間軸為「62px 時刻｜內容」（768px 以上 76px；編輯模式 52／1fr 並加上移、下移與拖曳把手），資訊鍵值為「72px 標籤｜值」，支出列為「36px 印章｜內容｜金額」。

**自適應版面（RWD）：** 767px 以下是單欄手機版（內容最寬 560px、底部五分頁）。768px 以上分頁列改為左側 92px 直欄（目前分頁以左側 3px 直條標示），內容寬 `min(1120px, 100vw − 92px)` 置中，間距 24px；總覽 8 天排兩欄、地圖兩欄、面板改為置中對話框。1024px 以上：單日頁左欄 340px 固定顯示當天資訊（sticky），右欄時間軸；分帳左欄 380px 結算與分段鈕，右欄明細；清單兩欄。

節奏以 4px 為底：元件內間距 4／8／12px，區塊間 16–22px。所有可點目標至少 40px，主要的 44–46px（圖示鈕 44、按鈕 46、輸入框 46、膠囊 42、FAB 54）。iOS safe-area 在頂列、分頁列與面板底部都有處理。

## Elevation & Depth

以平面為主：頁面內容不浮起，靠卡紙（#f3f5f7）與白頁（#ffffff）的色階差、加上 1px 髮線分隔來分層。陰影只屬於「蓋在內容上」的浮層。深色模式沿用相同陰影，層次主要靠底色由深藍黑往上提亮。

### Shadow Vocabulary
- **面板上緣陰影**（`box-shadow: 0 -10px 32px rgba(0, 0, 0, .18)`）：底部面板，背後再加 `rgba(12, 20, 40, .42)` 遮罩。
- **浮動按鈕陰影**（`box-shadow: 0 6px 16px rgba(0, 0, 0, .22), 0 1px 3px rgba(0, 0, 0, .18)`）：分帳頁的「記一筆」FAB。
- **提示陰影**（`box-shadow: 0 8px 20px rgba(0, 0, 0, .2)`）：toast 提示條。
- **拖曳陰影**（`box-shadow: 0 8px 20px rgba(0, 0, 0, .14)`）：編輯模式中被拖起的那一站。

### Named Rules
**The Hairline Rule.** 內容區不用陰影卡片；列與列之間是 1px 髮線，區塊之間是髮線或虛線。陰影只給面板、FAB、提示與拖曳中的項目。

## Shapes

形狀語言是「圓章＋柔角矩形」。真正的圓只屬於印章：外圈 3px、內圈 1.3px 的雙圈，套上 SVG 擾動濾鏡產生油墨毛邊與缺墨，並依站點 id 固定傾斜 −11° 到 +7°。其他元件一律是圓角矩形或膠囊：小標籤 4px、輸入框與分段 10px、按鈕與圖示鈕 12px、底部面板上緣 18px、膠囊與 FAB 全圓。邊框統一 1px（印章選項與標籤用 1.2–1.5px 的 currentColor 外框），虛線只用於「未蓋章」空圈、移動段落的左側導引線與住宿之間的分隔。

### Named Rules
**The Round Seal Rule.** 正圓留給印章；其他元件不做成圓形徽章，避免和分帳的印章混淆。

## Components

### Buttons
樸素、厚實、可單手按的實心按鈕。
- **Shape:** 柔角（12px），最小高 46px，左右 18px，字 15px／700，可帶 19px 線條圖示。
- **Primary:** 海軍藍底白字（例如「導航」）；深色模式改用深一階海軍藍。
- **Default:** 白頁底、墨色字、粗髮線外框（例如撥電話、關閉、編輯這一站）。
- **Hover / Focus:** 無 hover 樣式；按下時縮到 0.97（0.15s），焦點為 2px 深一階海軍藍外框、外推 2px。
- **Danger:** 白底、警示紅字、45% 警示紅外框；第一次按下變成「再按一次確認刪除」的警示紅實心狀態，3 秒後恢復。
- **Link:** 無底線框的文字按鈕，深一階海軍藍、700、底線外推 3px。

### Chips
- **Style:** 全圓膠囊，高 42px，粗髮線外框，14.5px／700；可在左側嵌入 24px 印章（付款人「我／伴」）。
- **State:** 選取時海軍藍底白字，嵌入的印章同時轉白、取消正片疊底。

### Cards / Containers
本系統沒有卡片牆。內容容器是全寬列表列，以髮線分隔：
- **Corner Style:** 列本身無圓角；只有「今天／下一站」捷徑（12px）、提醒條與橫幅（10px）、地圖圖片（12px）是圓角區塊。
- **Background:** 卡紙底上的白頁區塊（結算區、提醒條），或直接透出卡紙。
- **Shadow Strategy:** 無，見 Elevation & Depth。
- **Border:** 1px 髮線。
- **Internal Padding:** 列 16px（上下）×16px（左右）；時間軸列 12px；提醒條 10px 12px。

### Inputs / Fields
- **Style:** 卡紙底（比面板低一階）、1px 粗髮線外框、10px 圓角、最小高 46px、16px 字（避免 iOS 自動放大）。金額欄用 Barlow 34px／700、高 62px。
- **Focus:** 外框消失，換成 2px 深一階海軍藍外框（offset 0）。
- **Error / Disabled:** 錯誤訊息為警示紅 14px／700；停用的圖示鈕降到 30% 不透明。
- **Status picker:** 五格並排的印章選項，每格 10px 圓角、髮線外框，選取時海軍藍外框加內框與 7% 海軍藍底。

### Navigation
- **頂列：** 海軍藍底、白字，標題 17px／800（其中數字 21px）；右側為白色 35% 外框的透明膠囊動作鈕，啟用時翻成白底海軍藍字。
- **底部分頁：** 五等分，白頁 94% 不透明＋飽和 1.4、模糊 14px，上緣髮線；23px 圖示＋11.5px／700 標籤，未選灰墨、目前頁海軍藍並在上緣加 3px 粗的短橫條。深色模式目前頁改墨色。
- **分段控制：** 分帳頁四格（總帳、每日、類別、結算），10px 圓角、白底粗髮線，選取時海軍藍實心。

### Stamp（印泥章，招牌元件）
雙圈加一個 Seal 印字的 SVG，顏色取自 `--ink-<tone>`，在淺色模式以正片疊底（multiply）壓在紙上、不透明度 0.95。只用在分帳：結算「済」76px、付款人 24–30px、匯率標記 22px。狀態改變（新增一筆、匯率由估轉實、結清）時播放「下壓蓋章」動畫：從 1.9 倍、多轉 14°、模糊 3px 落下，壓到 0.92 再回彈到 1，共 0.5s（`cubic-bezier(.16, 1, .3, 1)`）。

### Bottom Sheet（底部面板）
原生 `<dialog>`，白頁底、上緣 18px 圓角、最高 92dvh，頂端 40×4px 粗髮線把手。開啟由下往上 40px 淡入（0.32s），關閉 0.18s ease-in 下沉。768px 以上改為置中對話框（四角 18px 圓角、無把手、最高 86dvh）。內部結構：標題、日文名、中繼資訊、動作按鈕列、鍵值表、查證段落，底部以髮線隔出「關閉／編輯」。

### Timeline（單日時間軸）
每站一列：左欄 Barlow 時刻（下一站轉朱色、該列鋪朱暈）、中欄站名與日文名、右欄印章。站與站之間的移動段落縮成細列，以虛線左導引線＋交通圖示表示。

### Settle（結算區）
分帳頁頂端的白頁區塊：一句「誰補誰」＋ Barlow 56px 台幣金額；結清後金額轉灰並畫刪除線，右上蓋上 76px 朱色「済」章。

## Do's and Don'ts

### Do:
- **Do** 行程端不顯示查證狀態，時間軸保持乾淨、不蓋章；查證內容寫在備註裡。
- **Do** 讓數字當主角：日數 52px、倒數 76px、結算 56px、時刻 21px，一律 Barlow Condensed 加 `tabular-nums`。
- **Do** 以 1px 髮線（#dce1e9）分隔列表，讓內容直接坐在卡紙底上。
- **Do** 狀態改變時用 0.5s 的下壓蓋章動畫回饋，並在 `prefers-reduced-motion` 時關閉動畫。
- **Do** 所有可點目標至少 40px，主要動作 44–46px，左右留白 16px。
- **Do** 深色模式只換 token 值；印章改成一般混合模式。

### Don't:
- **Don't** 做白卡片牆或日期膠囊分頁；日期用列表與大日數呈現。
- **Don't** 把朱色用在按鈕、裝飾或警示；刪除與錯誤用警示紅（#b3261e）。
- **Don't** 給內容列或區塊加陰影；陰影只屬於面板、FAB、提示與拖曳中的項目。
- **Don't** 在印章以外使用 Seal 字型，也不要在印章裡放子集以外的字。
- **Don't** 用正圓形徽章表示印章以外的東西。
