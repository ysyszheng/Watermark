import numpy as np
from PIL import Image, ImageDraw,ImageFont
import argparse

def addWatermark(image_path,text):
    image=Image.open(image_path)
    draw = ImageDraw.Draw(image)
    draw.text((50,50),text)

    image.save('output.png') 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="watermarker")
    parser.add_argument('-i','--image',type=str,help="input image")
    parser.add_argument('-w','--watermark',type=str,help="input watermark")
    args = parser.parse_args()

    addWatermark(args.image, args.watermark)