import numpy as np
from PIL import Image, ImageDraw,ImageFont
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="watermarker")
    parser.add_argument('-i','--image',type=str,help="input image")
    parser.add_argument('-w','--watermarker',type=str,help="input watermarker")
    args = parser.parse_args()

    image=Image.open(args.image)
    draw = ImageDraw.Draw(image)
    draw.text((50,50),args.watermarker)

    image.save('output.png')