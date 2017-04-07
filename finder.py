
from PIL import Image, ImageChops
import glob

def comp(im, im2):


    diff = ImageChops.difference(im, im2)
    return diff.getdata()
im = Image.open('textures/eyes/man/eyeroll0001.jpg')
out = Image.new(im.mode, im.size)
out_pixels = list(out.getdata())


f = iter(glob.glob('textures/eyes/man/eyeroll*.jpg'))
cur = None
while True:
    try:
        if not cur:
            cur = Image.open(f.next())
        d = Image.open(f.next())
        x = comp(cur, d)
        cur = d
        new_out = []
        for _ in zip(out_pixels, x):
            new_out.append((_[0][0] + _[1][0], _[0][1] + _[1][1], _[0][2] + _[1][2]))
        out_pixels = new_out
    except StopIteration as e:
        break

new_out = []
#for op in out_pixels:
#    if op[0] > 200:
    #    new_out.append(op)
#    else:
    #    new_out.append((0, 0, 0))
out.putdata(out_pixels)

out.save('textures/eyes/man/eyes.jpg')
