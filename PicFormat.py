#!/usr/bin/env python3

import argparse
from PIL import Image, ImageOps


def main():
    parser = argparse.ArgumentParser(
        description="Apply a negative/invert filter to an image."
    )
    parser.add_argument("infile", help="Input image file")
    parser.add_argument("outfile", help="Output image file")

    args = parser.parse_args()

    try:
        image = Image.open(args.infile).convert("RGB")
        negative = ImageOps.invert(image)
        negative.save(args.outfile)

        print(f"Created: {args.outfile}")

    except FileNotFoundError:
        print(f"Error: input file not found: {args.infile}")
    except Exception as e:
        print(f"Error processing image: {e}")


if __name__ == "__main__":
    main()