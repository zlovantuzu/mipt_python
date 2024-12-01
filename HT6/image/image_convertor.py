from HT6.image.image import MonochromeImage, ColorImage, BinaryImage
from scipy.ndimage import distance_transform_edt
import numpy as np


class ImageConverter:
    @staticmethod
    def binary_to_binary(image):
        return image

    @staticmethod
    def binary_to_monochrome(image):
        binary_array = np.array(image.data)
        distance_map = distance_transform_edt(binary_array == 0)
        max_distance = distance_map.max()

        monochrome_image = MonochromeImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                normalized_value = int((distance_map[y, x] / max_distance) * 255)
                monochrome_image.set_pixel(x, y, normalized_value)
        return monochrome_image

    @staticmethod
    def binary_to_color(image, palette):
        monochrome_image = ImageConverter.binary_to_monochrome(image)
        return ImageConverter.monochrome_to_color(monochrome_image, palette)

    @staticmethod
    def monochrome_to_binary(image, threshold=128):
        binary_image = BinaryImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                binary_image.set_pixel(x, y, 1 if image.data[y][x] >= threshold else 0)
        return binary_image

    @staticmethod
    def monochrome_to_monochrome(image, factor=1.0, offset=0):
        corrected_image = MonochromeImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                corrected_value = int(image.data[y][x] * factor + offset)
                corrected_value = max(0, min(255, corrected_value))
                corrected_image.set_pixel(x, y, corrected_value)
        return corrected_image

    @staticmethod
    def monochrome_to_color(image, palette):
        color_image = ColorImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                gray = image.data[y][x]
                r, g, b = palette[gray]
                color_image.set_pixel(x, y, r, g, b)
        return color_image

    @staticmethod
    def color_to_binary(image, threshold=128):
        monochrome_image = ImageConverter.color_to_monochrome(image)
        return ImageConverter.monochrome_to_binary(monochrome_image, threshold)

    @staticmethod
    def color_to_monochrome(image):
        monochrome_image = MonochromeImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.data[y][x]
                gray = int((r + g + b) / 3)
                monochrome_image.set_pixel(x, y, gray)
        return monochrome_image

    @staticmethod
    def color_to_color(image, r_factor=1.0, g_factor=1.0, b_factor=1.0):
        corrected_image = ColorImage(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.data[y][x]
                corrected_r = max(0, min(255, int(r * r_factor)))
                corrected_g = max(0, min(255, int(g * g_factor)))
                corrected_b = max(0, min(255, int(b * b_factor)))
                corrected_image.set_pixel(x, y, corrected_r, corrected_g, corrected_b)
        return corrected_image
