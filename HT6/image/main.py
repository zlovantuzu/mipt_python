import numpy as np
from PIL import Image as PILImage
from HT6.image.image import BinaryImage, MonochromeImage, ColorImage
from HT6.image.image_convertor import ImageConverter


def read_image_from_file(filepath, image_type):
    pil_image = PILImage.open(filepath)

    image_array = np.array(pil_image)

    if image_type == 'binary':
        binary_image = BinaryImage(pil_image.width, pil_image.height)
        if len(image_array.shape) == 3:  # RGB
            grayscale_image = np.mean(image_array, axis=2).astype(int)  # Среднее по RGB
        else:
            grayscale_image = image_array
        for y in range(pil_image.height):
            for x in range(pil_image.width):
                binary_value = 1 if grayscale_image[y][x] > 128 else 0
                binary_image.set_pixel(x, y, binary_value)
        return binary_image

    elif image_type == 'monochrome':
        if len(image_array.shape) == 3:  # Если изображение RGB
            image_array = np.mean(image_array, axis=2).astype(int)  # Преобразование в оттенки серого
        monochrome_image = MonochromeImage(pil_image.width, pil_image.height)
        if len(image_array.shape) == 3:  # RGB
            grayscale_image = np.mean(image_array, axis=2).astype(int)
        else:
            grayscale_image = image_array
        for y in range(pil_image.height):
            for x in range(pil_image.width):
                monochrome_image.set_pixel(x, y, int(grayscale_image[y][x]))
        return monochrome_image

    elif image_type == 'color':
        if len(image_array.shape) != 3 or image_array.shape[2] != 3:
            raise ValueError("Изображение не является цветным RGB.")
        color_image = ColorImage(pil_image.width, pil_image.height)
        for y in range(pil_image.height):
            for x in range(pil_image.width):
                r, g, b = image_array[y][x]
                color_image.set_pixel(x, y, int(r), int(g), int(b))
        return color_image

    else:
        raise ValueError("Неверный тип изображения. Используйте 'binary', 'monochrome' или 'color'.")


def save_image_to_file(image, filepath):
    from PIL import Image as PILImage
    import numpy as np

    if isinstance(image, BinaryImage):
        binary_array = np.array(image.data) * 255  # Преобразуем 0/1 в 0/255
        pil_image = PILImage.fromarray(binary_array.astype(np.uint8), mode="L")

    elif isinstance(image, MonochromeImage):
        mono_array = np.array(image.data)
        pil_image = PILImage.fromarray(mono_array.astype(np.uint8), mode="L")

    elif isinstance(image, ColorImage):
        color_array = np.array(image.data)
        pil_image = PILImage.fromarray(color_array.astype(np.uint8), mode="RGB")

    else:
        raise ValueError("Неподдерживаемый тип изображения для сохранения.")

    # Сохраняем файл
    pil_image.save(filepath)
    print(f"Изображение сохранено в файл: {filepath}")


palette = {i: (i, 255 - i, i // 2) for i in range(256)}

binary_image = read_image_from_file("binary_image.png", "binary")
color_binary_image = ImageConverter.binary_to_color(binary_image, palette)
save_image_to_file(color_binary_image, "color_image_output.png")

monochrome_image = read_image_from_file("monochrome_image.png", "monochrome")
bin_mono_image = ImageConverter.monochrome_to_binary(monochrome_image)
save_image_to_file(bin_mono_image, "binary_image_output.png")

color_image = read_image_from_file("color_image.png", "color")
mono_color_image = ImageConverter.color_to_monochrome(color_image)
save_image_to_file(mono_color_image, "mono_image_output.png")


