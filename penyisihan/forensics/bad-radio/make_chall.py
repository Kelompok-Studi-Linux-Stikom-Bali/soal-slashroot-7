import string
import random
import math
import gizeh
from base64 import b64encode, b64decode
from moviepy.editor import *

FAKE_FLAG_1 = "slashroot7{oops_try_again}"
FAKE_FLAG_2 = "slashroot7{nah_youre_not_there_yet}"
FAKE_FLAG_3 = "slashroot7{alm0st_th3r3}"
FLAG = "slashroot7{R4di0_h4s_B33n_T0uhoU_h1JAck3D_w_4pPPl3_Z0MG}"


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


obfuscated_flag = "Hiya, it's been a while. Welcome to SLASHROOT 7.0. If you can see this, it means that you have successfully decoded this message, with layers upon layers of obfuscation I can throw into it. The string I'm about to give you is the final piece of this challenge. I'm sure you'll understand it. Good luck! " + \
    b64encode(FAKE_FLAG_1.encode()).decode() + "_" + b64encode(FAKE_FLAG_2.encode()).decode() + \
    "_" + b64encode(FAKE_FLAG_3.encode()).decode() + \
    "_" + b64encode(FLAG.encode()).decode()

print(FLAG)
print(obfuscated_flag)

original_clip = VideoFileClip("doksli.webm")


def make_frame(t):
    surface = gizeh.Surface(
        width=original_clip.size[0], height=original_clip.size[1])
    idx = int(t / (1.0 / float(original_clip.fps) * 8)) % len(obfuscated_flag)

    if idx < len(obfuscated_flag):
        bin_str = '{:08b}'.format(ord(obfuscated_flag[idx]))
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
final_clip.write_videofile("chall.webm")
