import math
import numpy
import struct
import csv
import json
import cv2

class HistEncoder:
    @staticmethod
    def encode(filename, data):
        raise NotImplementedError()

class BinHistEncoder(HistEncoder):
    @staticmethod
    def encode(filename, data):
        values = [data[i] for i in range(len(data))]
        with open(filename, 'wb') as file:
            file.write(struct.pack('f' * 256, *values))
        return


class CsvHistEncoder(HistEncoder):
    @staticmethod
    def encode(filename, data):
        data_as_strings = {str(key): str(value) for key, value in data.items()}

        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in data_as_strings.items():
                writer.writerow([key, value])


class TxtHistEncoder(HistEncoder):
    @staticmethod
    def encode(filename, data):
        with open(filename, "w") as file:
            for key, value in data.items():
                file.write(f"{key} {value} ")


class JsonHistEncoder(HistEncoder):
    @staticmethod
    def encode(filename, data):
        with open(filename, 'w') as file:
            json_data = {
                "keys": list(data.keys()),
                "values": list(data.values())
            }
            json.dump(json_data, file)


class ImageHistEncoder(HistEncoder):
    @staticmethod
    def encode(filename, data):
        total_pixels = sum(int(freq * 1e6) for freq in data.values())
        image_side = math.ceil(math.sqrt(total_pixels))
        image_size = (image_side, image_side)

        pixel_counts = {level: int(image_side ** 2 * freq) for level, freq in data.items()}

        pixels = []
        for level, count in pixel_counts.items():
            pixels.extend([level] * count)

        # если недостаточно пикселей
        while len(pixels) < image_size[0] * image_size[1]:
            pixels.append(0)

        # если пикселей больше чем нужно
        pixels = pixels[:image_size[0] * image_size[1]]

        image = numpy.array(pixels, dtype=numpy.uint8).reshape(image_size)
        cv2.imwrite(filename, image)
