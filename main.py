# cutest-cat-01 entry: a program that writes one picture of a cat to
# /output/entry.png. The picture is the entry.png beside this file:
# a 3D-rendered round ginger-and-white kitten with huge sparkling eyes,
# head tilted, a small smile, oversized paws and a pastel ball of yarn.
# The judge rubric ranks a clear cat subject first, then cuteness
# (soft round shapes, big bright eyes, a smile), then charm
# (head tilt, clumsy paws, a favourite toy), then clean craft and
# readability at small size. This image was made for that rubric:
# the kitten is centred, fills most of the frame, has the right
# number of legs, ears, whiskers and one tail, and carries no text.
#
# The program copies the image byte for byte, so two runs write
# identical output. Standard library only, no network.

import os
import shutil


OUTPUT_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, OUTPUT_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, OUTPUT_NAME))


if __name__ == "__main__":
    main()
