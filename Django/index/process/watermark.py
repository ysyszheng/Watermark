import numpy as np
from PIL import Image, ImageDraw,ImageFont
import argparse

def addWatermark(image,text):
    draw = ImageDraw.Draw(image)
    draw.text((50,50),text)
    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="watermarker")
    parser.add_argument('-i','--image',type=str,help="input image")
    parser.add_argument('-w','--watermark',type=str,help="input watermark")
    args = parser.parse_args()

    addWatermark(args.image, args.watermark)