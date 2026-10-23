import sys, json, os, subprocess
from multiprocessing import Pool
from PIL import Image, ImageOps
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from segment import segment
CROPS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crops')
os.environ['OMP_THREAD_LIMIT'] = '1'


def run(job):
    out = subprocess.run(['tesseract', job[-1], '-', '--psm', '6', '-l', 'eng'],
                         capture_output=True, text=True).stdout
    return list(job[:-1]) + [' '.join(out.split())]


if __name__ == '__main__':
    os.makedirs(CROPS, exist_ok=True)
    jobs = []
    for f in sys.argv[2:]:
        w, h, blocks = segment(f)
        im = Image.open(f).convert('L')
        stem = os.path.basename(f).replace(' ', '_').replace('&', 'and')
        for i, (k, y0, y1) in enumerate(blocks):
            if k == 'header':
                box = (int(0.07 * w), y0, int(0.95 * w), y1)
            else:
                box = (int(0.08 * w), y0, int(0.80 * w), y1)
            c = im.crop(box)
            c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
            c = ImageOps.expand(c, border=20, fill=c.getpixel((0, 0)))
            p = os.path.join(CROPS, f'{stem}_{i:04d}.png')
            c.save(p)
            jobs.append((f, i, k, y0, y1, p))
        print('cropped', f, len(blocks), flush=True)
    with Pool(4) as pool:
        res = pool.map(run, jobs, chunksize=4)
    json.dump(res, open(sys.argv[1], 'w'), indent=0)
    print('done', len(res))
