"""把 北陸自駕行程.xlsx 轉成網頁用的 data/trip.json 與 data/maps/*.webp。

只在初始化時執行一次；之後行程以網頁（手機）上的編輯為準。
用法：python tools/xlsx_to_json.py 北陸自駕行程.xlsx
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile

import openpyxl

SRC = sys.argv[1] if len(sys.argv) > 1 else '北陸自駕行程.xlsx'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data')

STATUS = {'✅': 'ok', '🟡': 'sec', '❗': 'call', '❌': 'bad', '—': 'na'}
DAY_DATES = ['2026-11-26', '2026-11-27', '2026-11-28', '2026-11-29',
             '2026-11-30', '2026-12-01', '2026-12-02', '2026-12-03']


def s(v):
    if v is None:
        return ''
    return str(v).strip()


def rows(ws, start=1):
    return [r for r in ws.iter_rows(min_row=start, values_only=True) if any(c is not None for c in r)]


wb = openpyxl.load_workbook(SRC)

# 總覽
ov = rows(wb['總覽'])
title = s(ov[0][0])
flights = [{'label': s(r[0]), 'text': s(r[1])} for r in ov if s(r[0]) in ('去程', '回程')]
days = []
for r in ov:
    m = re.match(r'Day (\d)', s(r[0]))
    if m:
        n = int(m.group(1))
        days.append({
            'n': n, 'date': DAY_DATES[n - 1], 'label': s(r[1]), 'title': s(r[2]),
            'stay': s(r[3]), 'note': s(r[5]), 'backup': s(r[6]),
        })

# 每日行程
stops = []
for i, r in enumerate(rows(wb['每日行程'], 2)):
    m = re.match(r'Day (\d)', s(r[0]))
    if not m:
        continue
    status = STATUS.get(s(r[15])[:1], 'na')
    stops.append({
        'id': 's%02d' % (i + 1), 'day': int(m.group(1)), 'time': s(r[2]),
        'stay': int(r[3]) if isinstance(r[3], (int, float)) else None,
        'type': s(r[4]) or '景點', 'name': s(r[5]), 'ja': s(r[6]), 'intro': s(r[7]),
        'reason': s(r[8]), 'hours': s(r[9]), 'closed': s(r[10]), 'fee': s(r[11]),
        'note': s(r[12]), 'address': s(r[13]), 'source': s(r[14]), 'status': status,
        'verify': s(r[16]), 'phone': s(r[17]), 'verifySource': s(r[18]),
        'verifyDate': s(r[19])[:10],
    })

# 住宿：欄＝住宿，列＝欄位
lw = rows(wb['住宿'])
lodging = []
for c in range(1, len(lw[0])):
    item = {s(r[0]): s(r[c]) for r in lw[1:]}
    lodging.append(item)

# 季節與風險
risk_rows = rows(wb['季節與風險'])
risks = {'weather': [], 'season': [], 'area': [], 'trip': []}
sec = None
for r in risk_rows:
    head = s(r[0])
    if head in ('天氣', '季節性', '區域風險', '行程風險') and not s(r[1]):
        sec = {'天氣': 'weather', '季節性': 'season', '區域風險': 'area', '行程風險': 'trip'}[head]
        continue
    if head in ('項目', '區域', '風險'):
        continue
    if sec == 'weather':
        risks['weather'].append(head)
    elif sec == 'season':
        risks['season'].append({'item': head, 'state': s(r[1]), 'text': s(r[2]), 'source': s(r[3])})
    elif sec == 'area':
        risks['area'].append({'area': head, 'kind': s(r[1]), 'level': s(r[2]), 'text': s(r[3]),
                              'advice': s(r[4]), 'check': s(r[5])})
    elif sec == 'trip':
        risks['trip'].append({'text': head, 'state': s(r[1])})

# 出發前清單
checklist = []
for i, r in enumerate(rows(wb['出發前清單'], 2)):
    if s(r[0]) in ('完成進度', '說明'):
        continue
    checklist.append({'id': 'c%02d' % (i + 1), 'cat': s(r[0]), 'text': s(r[1]),
                      'done': s(r[2]).upper() == 'Y', 'note': s(r[3])})

# 查證說明
legend = {s(r[0]): s(r[1]) for r in rows(wb['查證說明'])}

# 地圖：drawing 錨點列 → 圖片；第 1 張是全程總覽，其後依序 Day 1–8
z = zipfile.ZipFile(SRC)
drawing = z.read('xl/drawings/drawing1.xml').decode()
rels = z.read('xl/drawings/_rels/drawing1.xml.rels').decode()
rid_to_img = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="\.\./media/([^"]+)"', rels))
rid_to_img.update({k: v for v, k in re.findall(r'Target="\.\./media/([^"]+)"[^>]*Id="(rId\d+)"', rels)})
anchors = re.findall(r'<xdr:row>(\d+)</xdr:row>.*?r:embed="(rId\d+)"', drawing, re.S)
anchors.sort(key=lambda a: int(a[0]))
os.makedirs(os.path.join(OUT, 'maps'), exist_ok=True)
maps = []
with tempfile.TemporaryDirectory() as tmp:
    for idx, (_, rid) in enumerate(anchors):
        name = 'overview' if idx == 0 else 'day%d' % idx
        src = os.path.join(tmp, rid_to_img[rid])
        open(src, 'wb').write(z.read('xl/media/' + rid_to_img[rid]))
        dst = os.path.join(OUT, 'maps', name + '.webp')
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-c:v', 'libwebp',
                        '-quality', '82', dst], check=True)
        maps.append({'key': name, 'src': 'data/maps/%s.webp' % name,
                     'day': None if idx == 0 else idx})

trip = {
    'version': 1, 'title': title, 'start': DAY_DATES[0], 'end': DAY_DATES[-1],
    'flights': flights, 'days': days, 'stops': stops, 'lodging': lodging,
    'risks': risks, 'checklist': checklist, 'legend': legend, 'maps': maps,
    'source': {'file': os.path.basename(SRC), 'verifiedOn': legend.get('查證日', '')[:10]},
}
with open(os.path.join(OUT, 'trip.json'), 'w', encoding='utf-8') as f:
    json.dump(trip, f, ensure_ascii=False, indent=1)
print('days', len(days), 'stops', len(stops), 'lodging', len(lodging),
      'checklist', len(checklist), 'maps', len(maps))
