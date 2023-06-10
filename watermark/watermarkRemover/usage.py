from main import WatermarkRemover

path = "./data/"


def remover(template, image_path, result_path):
    watermark_template_filename = template
    remover = WatermarkRemover()
    remover.load_watermark_template(watermark_template_filename)

    remover.remove_watermark(image_path, result_path)


if __name__ == "__main__":
    remover(
        path + "anjuke-watermark-template.jpg",
        path + "anjuke2.jpg",
        path + "result.jpg",
    )
