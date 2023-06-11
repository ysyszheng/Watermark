import argparse

from PIL import Image, ImageDraw, ImageFont


def addWatermark(image_path, text):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font_size = int(image.size[1] / 10)
    font = ImageFont.truetype(
        "/usr/share/fonts/dejavu/DejaVuSansCondensed-Bold.ttf", font_size
    )
    fill_color = (255, 255, 255, 128)
    draw.text((50, 50), text, font=font, fill=fill_color)

    image.save("output.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="watermarker")
    parser.add_argument("-i", "--image", type=str, help="input image")
    parser.add_argument("-w", "--watermark", type=str, help="input watermark")
    args = parser.parse_args()

    addWatermark(args.image, args.watermark)
