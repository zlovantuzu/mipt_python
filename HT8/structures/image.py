import cv2

"""
Абстрактная фабрика 
"""


class AbstractFactoryImageReader():
    def read_image(self, file_path):
        raise NotImplementedError()


class BinImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        # >127 => 255, <127 => 0
        _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        return binary_image


class MonochromeImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        return image


class ColorImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        return cv2.imread(file_path, cv2.IMREAD_COLOR)


def get_image_reader(ident):
    if ident == 0:
        return BinImageReader()
    elif ident == 1:
        return MonochromeImageReader()
    elif ident == 2:
        return ColorImageReader()


if __name__ == "__main__":
    try:
        for i in range(3):
            print(get_image_reader(i))
    except Exception as e:
        print(e)
