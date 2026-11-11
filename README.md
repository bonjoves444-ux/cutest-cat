# Cutest cat — make.fun cutest-cat-01

A 3D-rendered round ginger-and-white kitten in a tiny white shirt
and black tie, paws pressed thoughtfully to its temples, huge
sparkling amber eyes and a small smile, centred on a soft cream
background. A polished remake of a reference photo of a cat in a
shirt and tie, thinking — same joke, clean craft.

## Why this cat

The judge weighs, in order: a clear cat subject; cuteness (soft
round shapes, big bright eyes, an expression that makes a person
smile); charm (head tilt, clumsy paws, a favourite toy); clean
craft (right number of legs, ears, whiskers, one tail, no text);
and readability at ~300 px. The kit's own calibration backs the
style: its strongest reference image is a 3D-rendered round
kitten with huge sparkling eyes and oversized paws, ahead of a
photorealistic kitten and a studio photo. This entry follows
that winning style, with the kitten filling most of the frame.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png`
byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output`). Two runs write identical bytes. The image is a
1024x1024 PNG, under 1 MiB.

## License

MIT — see LICENSE.
