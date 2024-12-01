class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = None

    def display(self):
        raise NotImplementedError("Метод display должен быть реализован в подклассе")

    def get_size(self):
        return self.width, self.height


class BinaryImage(Image):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = [[0 for _ in range(width)] for _ in range(height)]  # 0 или 1

    def set_pixel(self, x, y, value):
        if value not in (0, 1):
            raise ValueError("Значение должно быть 0 или 1")
        self.data[y][x] = value

    def display(self):
        for row in self.data:
            print("".join(str(pixel) for pixel in row))


class MonochromeImage(Image):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = [[0 for _ in range(width)] for _ in range(height)]  # Оттенки серого: 0-255

    def set_pixel(self, x, y, value):
        if not (0 <= value <= 255):
            raise ValueError("Значение должно быть в диапазоне 0-255")
        self.data[y][x] = value

    def display(self):
        for row in self.data:
            print(" ".join(f"{pixel:3}" for pixel in row))


class ColorImage(Image):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]  # RGB

    def set_pixel(self, x, y, r, g, b):
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("Значения RGB должны быть в диапазоне 0-255")
        self.data[y][x] = [r, g, b]

    def display(self):
        for row in self.data:
            print(" ".join(f"({r},{g},{b})" for r, g, b in row))

