import json, re, sys, os
from collections import OrderedDict

NAMES = {
    'anatomy.png': 'Anatomy', 'physiology.png': 'Physiology', 'biochemistry .png': 'Biochemistry',
    'Pathology.png': 'Pathology', 'Pharmacology.png': 'Pharmacology',
    'Forensic Medicine.png': 'Forensic Medicine', 'Community Medicine.png': 'Community Medicine',
    'ENT.png': 'ENT', 'Ophthalmology.png': 'Ophthalmology', 'Medicine.png': 'Medicine',
    'Surgery.png': 'Surgery', 'Obstetrics & Gynaecology v.png': 'Obstetrics & Gynaecology',
    'Paediatrics.png': 'Paediatrics', 'Orthopaedics.png': 'Orthopaedics',
    'Dermatology.png': 'Dermatology', 'Psychiatry.png': 'Psychiatry',
    'Anaesthesia.png': 'Anaesthesia', 'Radiology.png': 'Radiology',
}
ORDER = list(NAMES.values())

ID_RE = re.compile(r'^\W*P\s*[MN]\s*[O0-9]{3,6}\s*[.,:;]?\s*')

def clean_id(raw):
    digits = re.sub(r'[^0-9Oo]', '', raw[raw.upper().find('M') + 1:] if 'M' in raw.upper() else raw)
    digits = digits.replace('O', '0').replace('o', '0')
    # app ids are PM + 4 digits; OCR reads "PM0955" as "PMO0955"
    if len(digits) > 4 and digits.startswith('00'):
        digits = digits[1:]
    return 'PM' + digits

def parse(res):
    data = OrderedDict((s, []) for s in ORDER)
    issues = []
    for f, i, kind, y0, y1, text in res:
        subj = NAMES[f]
        if kind == 'header':
            data[subj].append({'subtopic': text, 'pearls': []})
            continue
        m = ID_RE.match(text)
        if not m:
            issues.append((subj, y0, text))
            pid, title = '', text
        else:
            pid, title = clean_id(m.group(0)), text[m.end():].strip()
        if not data[subj]:
            data[subj].append({'subtopic': '(untitled)', 'pearls': []})
        data[subj][-1]['pearls'].append({'id': pid, 'title': title, 'y': y0})
    return data, issues

if __name__ == '__main__':
    res = json.load(open(sys.argv[1]))
    data, issues = parse(res)
    json.dump(data, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
    for s, subs in data.items():
        print(f'{s}: {len(subs)} subtopics, {sum(len(x["pearls"]) for x in subs)} pearls')
    print('unparsed:', len(issues))
    for x in issues: print('  ', x)
