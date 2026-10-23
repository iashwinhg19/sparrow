import sys, json, glob, os
from PIL import Image

def near(p, q, tol=6):
    return all(abs(a-b) <= tol for a, b in zip(p, q))

HDR = (229, 240, 243)
SEP = (228, 228, 228)

def segment(path):
    im = Image.open(path).convert('RGB')
    w, h = im.size
    px = im.load()
    xa, xb = int(0.9*w), int(0.5*w)
    kinds = []
    for y in range(h):
        a, b = px[xa, y], px[xb, y]
        if near(a, HDR, 3):
            kinds.append('H')
        elif near(a, SEP, 3) and near(b, SEP, 3):
            kinds.append('S')
        else:
            kinds.append('.')
    # runs
    runs = []
    y = 0
    while y < h:
        k = kinds[y]; y2 = y
        while y2 < h and kinds[y2] == k: y2 += 1
        runs.append((k, y, y2)); y = y2
    blocks = []
    started = False
    for i, (k, y0, y1) in enumerate(runs):
        if k == 'H' and y1 - y0 > 15:
            blocks.append(('header', y0, y1)); started = True
        elif k == '.' and started and y1 - y0 > 30:
            blocks.append(('item', y0, y1))
    return w, h, blocks

if __name__ == '__main__':
    for f in sys.argv[1:]:
        w, h, b = segment(f)
        print(f, sum(1 for x in b if x[0]=='header'), sum(1 for x in b if x[0]=='item'))
