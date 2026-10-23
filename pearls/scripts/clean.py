"""Turn raw OCR rows into a clean subject -> subtopic -> pearl structure."""
import json, re, sys
from collections import OrderedDict
from parse import NAMES, ORDER

PM_RE = re.compile(r'^\W*P\s*[MN]\s*([O0-9]{3,6})\s*[.,:;]?\s*')
SECOND_PM = re.compile(r'\s+P\s*M\s*[O0-9]{3,5}\b.*$')
BAD_HEADERS = {'mut', 'Wwtliwiw'}

CUT = 'Cut off at the bottom of the screenshot; title incomplete'
# (subject, raw y of the OCR row) -> (id, title, note); None drops the row
ROW_FIXES = {
    ('Anaesthesia', 15493): ('PM0494', 'Muscle Relaxant and Effect on Cardiac Muscarinic Receptors', ''),
    ('Community Medicine', 36437): ('PM1144', 'Surgical A…', CUT + '; ID partly hidden'),
    ('Paediatrics', 15581): ('PM2064', 'Thalassemia syndromes', 'Partly cut off at the bottom of the screenshot'),
    ('Physiology', 33801): ('PM2479', 'Physiologic effects of …', CUT),
    ('Paediatrics', 14756): None,  # Endocrine pearl repeated inside a seam
    ('ENT', 13430): ('PM1097', 'Lymph Node Levels in the Neck', ''),
    ('Obstetrics & Gynaecology', 20843): ('PM2497', 'Uterine Signs in P…', CUT),
    ('Psychiatry', 12227): ('PM2059', "BNS section 22, M'Naghten's rule",
                            'Title cut off in the screenshot; completed from the same pearl in Forensic Medicine'),
}
ID_FIXES = {'PM19839': 'PM1989', 'PM16771': 'PM1671'}
RAW_FIXES = {'PMO075/7.': 'PM0757.', 'PMO02339.': 'PM0239.'}
TITLE_FIXES = {
    'Foster-—Kennedy Syndrome': 'Foster-Kennedy Syndrome',
    'Structural Alterations of the 8 -Globin Gene': 'Structural Alterations of the β-Globin Gene',
    'Carbamoy! phosphate synthetase | & Il': 'Carbamoyl phosphate synthetase I & II',
    'MHC Classes | and II': 'MHC Classes I and II',
    'Comparative Features of Type | and Type II Diabetes mellitus':
        'Comparative Features of Type I and Type II Diabetes mellitus',
}

# l/I confusions and line-break hyphens left by OCR
WORD_FIXES = [
    (r'\blon\b', 'Ion'), (r'\blonising\b', 'Ionising'), (r'\blvermectin\b', 'Ivermectin'),
    (r'\bAlDS\b', 'AIDS'), (r'\bGl\b', 'GI'), (r'\bMl\b', 'MI'), (r'\blla\b', 'IIa'), (r'^Nat - K\+', 'Na+ - K+'),
    (r'(?<=[a-z0-9])- (?=[a-z0-9])', '-'), (r'(?<=ICD)- ', '-'), (r'\bCL-', 'Cl-'), (r'\b(Non|Ehler|Peutz|Salter)—', r'\1-'),
    (r'(?<=[a-z])—(?=[a-z])', '-'),
]


def fix_words(title):
    for pat, rep in WORD_FIXES:
        title = re.sub(pat, rep, title)
    return title


def norm_id(digits):
    digits = digits.replace('O', '0')
    if len(digits) == 3:
        digits = '0' + digits
    if len(digits) == 5 and digits[0] == '0':
        digits = digits[1:]
    return ID_FIXES.get('PM' + digits, 'PM' + digits)


def clean(res):
    data = OrderedDict((s, OrderedDict()) for s in ORDER)
    for f, _, kind, y0, _, text in res:
        subj = NAMES[f]
        subs = data[subj]
        if kind == 'header':
            if text in BAD_HEADERS:
                continue
            cur = text
            subs.setdefault(cur, OrderedDict())
            data[subj]['__cur'] = cur
            continue
        cur = subs.get('__cur')
        fix = ROW_FIXES.get((subj, y0), False)
        if fix is None:
            continue
        if fix:
            pid, title, note = fix
        else:
            for bad, good in RAW_FIXES.items():
                if text.startswith(bad):
                    text = good + text[len(bad):]
            m = PM_RE.match(text)
            if not m:
                continue  # seam debris with no pearl in it
            pid = norm_id(m.group(1))
            title = SECOND_PM.sub('', text[m.end():]).strip()
            title = fix_words(TITLE_FIXES.get(title, title))
            note = ''
        pearls = subs[cur]
        old = pearls.get(pid)
        # seam repeats: keep the shortest reading, since garbled ones carry extra text
        if old is None or len(title) < len(old['title']):
            pearls[pid] = {'id': pid, 'title': title, 'note': note}
    out = OrderedDict()
    for subj, subs in data.items():
        subs.pop('__cur', None)
        out[subj] = [{'subtopic': k, 'pearls': list(v.values())} for k, v in subs.items() if v]
    return out


if __name__ == '__main__':
    out = clean(json.load(open(sys.argv[1])))
    json.dump(out, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
    rows = uniq = 0
    for s, subs in out.items():
        n = sum(len(x['pearls']) for x in subs)
        u = len({p['id'] for x in subs for p in x['pearls']})
        rows += n; uniq += u
        print(f'{s}: {len(subs)} subtopics, {n} rows, {u} unique pearls')
    print('total rows', rows, 'unique per subject', uniq)
