import copy

from HT8.decoders.decoder import BinHistDecoder, TxtHistDecoder, JsonHistDecoder, CsvHistDecoder, ImageHistDecoder
import HT8.encoders.encoder

"""
Стратегия (Strategy)
"""


class Hist:
    @classmethod
    def read(cls, file_path):
        ext = file_path.rsplit('.', 1)[-1]
        if ext == 'bin':
            decoder = BinHistDecoder
        elif ext == 'txt':
            decoder = TxtHistDecoder
        elif ext == 'json':
            decoder = JsonHistDecoder
        elif ext == 'csv':
            decoder = CsvHistDecoder
        elif ext in ('png', 'jpg', 'jpeg', 'bmp'):
            decoder = ImageHistDecoder
        else:
            raise RuntimeError('Невозможно получить данные %s' % file_path)
        data = decoder.decode(file_path)
        return cls(data)

    def write(self, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'bin':
            encoder = HT8.encoders.encoder.BinHistEncoder
        elif ext == 'txt':
            encoder = HT8.encoders.encoder.TxtHistEncoder
        elif ext == 'json':
            encoder = HT8.encoders.encoder.JsonHistEncoder
        elif ext == 'csv':
            encoder = HT8.encoders.encoder.CsvHistEncoder
        elif ext in ('png', 'jpg', 'jpeg', 'bmp'):
            encoder = HT8.encoders.encoder.ImageHistEncoder
        else:
            raise RuntimeError('Невозможно записать данные %s' % filename)
        encoder.encode(filename, self._data)
        return

    def __init__(self, data):
        self._data = data

    def get_data(self):
        return copy.deepcopy(self._data)


if __name__ == "__main__":
    hist = Hist.read('../data/csv_test.csv')
    print(hist.get_data())
    hist.write('../data/csv_test_res.csv')

    hist = Hist.read('../data/1.jpg')
    print(hist.get_data())
    hist.write('../data/1_res_h.jpg')

    hist = Hist.read('../data/1.jpg')
    print(hist.get_data())
    hist.write('../data/1_res_h.json')
