"""contact.py -- tile rendered slide PNGs into 2x2 sheets for quick review.
Usage: python contact.py <dir-with-slide-NN.png>"""
import glob, os, sys
from PIL import Image

src = sys.argv[1]
files = sorted(glob.glob(os.path.join(src, "slide-*.png")))
tw, th = 960, 540
for k in range(0, len(files), 4):
    sheet = Image.new("RGB", (tw * 2 + 10, th * 2 + 10), "gray")
    for i, f in enumerate(files[k:k + 4]):
        im = Image.open(f).convert("RGB").resize((tw, th))
        sheet.paste(im, ((i % 2) * (tw + 10), (i // 2) * (th + 10)))
    out = os.path.join(src, f"sheet-{k // 4 + 1:02d}.png")
    sheet.save(out)
    print(out)
