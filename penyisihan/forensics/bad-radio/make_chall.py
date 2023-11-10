import string
import random
import math
import gizeh
from base64 import b64encode, b64decode
from moviepy.editor import *


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


FLAG_SEGMENTS = [
    "1:R4di0",
    "2:h4s",
    "3:b33n",
    "4:T0uhoU",
    "5:h1JAck3D",
    "6:w",
    "7:4pPPl3",
    "8:Z0MG"
]

OPENER = "Welcome to SLASHROOT 7.0. If you can see this, it means that you have successfully decoded this message, with layers upon layers of obfuscation I can throw into it. The string I'm about to give you is the final piece of this challenge. I'm sure you'll understand it. A hint: slashroot7\{1_2_3_4_5_6_7_8\}  Good luck! "

FLAG_OBFUSCATED = \
    random_string(42) + "((((" + b64encode(FLAG_SEGMENTS[0].encode()).decode() + "))))" + \
    random_string(50) + "((((" + b64encode(FLAG_SEGMENTS[1].encode()).decode() + "))))" + \
    random_string(64) + "((((" + b64encode(FLAG_SEGMENTS[2].encode()).decode() + "))))" + \
    random_string(40) + "((((" + b64encode(FLAG_SEGMENTS[3].encode()).decode() + "))))" + \
    random_string(70) + "((((" + b64encode(FLAG_SEGMENTS[4].encode()).decode() + "))))" + \
    random_string(34) + "((((" + b64encode(FLAG_SEGMENTS[5].encode()).decode() + "))))" + \
    random_string(72) + "((((" + b64encode(FLAG_SEGMENTS[6].encode()).decode() + "))))" + \
    random_string(44) + \
    "((((" + b64encode(FLAG_SEGMENTS[7].encode()).decode() + ")))) "


COMBINED = OPENER + FLAG_OBFUSCATED

print(FLAG_SEGMENTS)
print(COMBINED)
print(len(COMBINED))

# quit()

original_clip = VideoFileClip("doksli.webm")


def make_frame(t):
    surface = gizeh.Surface(
        width=original_clip.size[0], height=original_clip.size[1])
    idx = int(t / (1.0 / float(original_clip.fps) * 2)) % len(COMBINED)
    print(str(idx) + "/" + str(len(COMBINED)))

    if idx < len(COMBINED):
        bin_str = '{:08b}'.format(ord(COMBINED[idx]))
        for idx, x in enumerate(bin_str):
            color = (1, 1, 1) if x == "1" else (0, 0, 0)
            rect = gizeh.rectangle(lx=32, ly=32, xy=(
                16 + (32 * idx), 16), fill=color)
            rect.draw(surface)

    return surface.get_npimage(transparent=True)


graphics_clip_mask = VideoClip(lambda t: make_frame(t)[:, :, 3] / 255.0,
                               duration=original_clip.duration, ismask=True)
graphics_clip = VideoClip(lambda t: make_frame(t)[:, :, :3],
                          duration=original_clip.duration).set_mask(graphics_clip_mask)

final_clip = CompositeVideoClip(
    [original_clip, graphics_clip])
final_clip.write_videofile("flag.webm")
