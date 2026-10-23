"""Write the cleaned pearls into a workbook: summary, master list, one tab per subject."""
import json, sys, csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

data = json.load(open(sys.argv[1]))
out_xlsx, out_csv = sys.argv[2], sys.argv[3]

FONT = 'Arial'
HEAD = Font(name=FONT, bold=True, color='FFFFFF')
HEAD_FILL = PatternFill('solid', fgColor='1F4E79')
BODY = Font(name=FONT)
NOTE = Font(name=FONT, italic=True, color='9C2A00')
THIN = Border(bottom=Side(style='thin', color='D9D9D9'))
WRAP = Alignment(wrap_text=True, vertical='top')

rows = []
for subj, subs in data.items():
    where = {}
    for s in subs:
        for p in s['pearls']:
            where.setdefault(p['id'], []).append(s['subtopic'])
    for s in subs:
        for p in s['pearls']:
            others = [x for x in where[p['id']] if x != s['subtopic']]
            rows.append([subj, s['subtopic'], p['id'], p['title'], '; '.join(others), p['note']])


def header(ws, names, widths):
    for c, (n, w) in enumerate(zip(names, widths), 1):
        cell = ws.cell(row=1, column=c, value=n)
        cell.font, cell.fill = HEAD, HEAD_FILL
        cell.alignment = Alignment(vertical='center')
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.freeze_panes = 'A2'
    ws.row_dimensions[1].height = 22


def body(ws, r, values, note_col=None):
    for c, v in enumerate(values, 1):
        cell = ws.cell(row=r, column=c, value=v)
        cell.font = NOTE if c == note_col else BODY
        cell.alignment = WRAP
        cell.border = THIN


wb = Workbook()
summ = wb.active
summ.title = 'Summary'
allp = wb.create_sheet('All Pearls')

# master list; G/H are helper flags the summary counts with COUNTIFS
header(allp, ['Subject', 'Subtopic', 'Pearl ID', 'Pearl', 'Also listed under', 'Note',
              'First in subject?', 'First in subtopic?'], [22, 34, 11, 70, 34, 40, 10, 10])
for i, r in enumerate(rows, 2):
    body(allp, i, r, note_col=6)
    allp.cell(row=i, column=7, value=f'=IF(COUNTIFS($A$2:A{i},A{i},$C$2:C{i},C{i})=1,1,0)').font = BODY
    allp.cell(row=i, column=8, value=f'=IF(COUNTIFS($A$2:A{i},A{i},$B$2:B{i},B{i})=1,1,0)').font = BODY
last = len(rows) + 1
allp.auto_filter.ref = f'A1:H{last}'
for col in 'GH':
    allp.column_dimensions[col].hidden = True

header(summ, ['Subject', 'Subtopics', 'Pearl listings', 'Unique pearls', 'Cross-listed pearls'],
       [26, 12, 15, 15, 20])
subjects = list(data)
rng = lambda c: f"'All Pearls'!${c}$2:${c}${last}"
for i, s in enumerate(subjects, 2):
    body(summ, i, [s])
    summ.cell(row=i, column=2, value=f'=COUNTIFS({rng("A")},A{i},{rng("H")},1)')
    summ.cell(row=i, column=3, value=f'=COUNTIF({rng("A")},A{i})')
    summ.cell(row=i, column=4, value=f'=COUNTIFS({rng("A")},A{i},{rng("G")},1)')
    summ.cell(row=i, column=5, value=f'=C{i}-D{i}')
    for c in range(2, 6):
        summ.cell(row=i, column=c).font = BODY
        summ.cell(row=i, column=c).number_format = '#,##0'
t = len(subjects) + 2
summ.cell(row=t, column=1, value='Total').font = Font(name=FONT, bold=True)
for c in range(2, 6):
    L = get_column_letter(c)
    cell = summ.cell(row=t, column=c, value=f'=SUM({L}2:{L}{t - 1})')
    cell.font = Font(name=FONT, bold=True)
    cell.number_format = '#,##0'
    cell.border = Border(top=Side(style='thin'))
notes = [
    'Source: the 18 subject screenshots in this repository, read with OCR and checked by hand at the stitching seams.',
    '"Pearl listings" counts every row; a pearl filed under two subtopics of one subject counts twice there and once in "Unique pearls".',
    'A few titles were cut off at the bottom of a screenshot and completed by hand; those rows carry a note in the All Pearls tab.',
    'Each subject list is complete: no pearls follow the last one shown in its screenshot.',
]
for k, n in enumerate(notes):
    c = summ.cell(row=t + 2 + k, column=1, value=n)
    c.font = Font(name=FONT, italic=True, color='595959')

# one tab per subject
for s in subjects:
    ws = wb.create_sheet(s.replace('&', 'and')[:31])
    header(ws, ['Subtopic', 'Pearl ID', 'Pearl', 'Also listed under', 'Note'], [34, 11, 70, 34, 40])
    r = 2
    for row in rows:
        if row[0] == s:
            body(ws, r, row[1:], note_col=5)
            r += 1
    ws.auto_filter.ref = f'A1:E{r - 1}'

wb.save(out_xlsx)
with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Subject', 'Subtopic', 'Pearl ID', 'Pearl', 'Also listed under', 'Note'])
    w.writerows(rows)
print(len(rows), 'rows')
