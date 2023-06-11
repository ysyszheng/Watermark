from main import WatermarkRemover

path = "./data/"


def remover(template_path, image_path, result_path):
    remover = WatermarkRemover()
    remover.load_watermark_template(template_path)
    remover.remove_watermark(image_path, result_path)


if __name__ == "__main__":
    remover(
        path + "test-template.jpg",
        path + "test.jpg",
        path + "result.jpg",
    )
