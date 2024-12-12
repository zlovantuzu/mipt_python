"""
Прототип - паттерн, порождающий объекты.
"""

import copy

from HT8.algorithms.object_analysis import BinaryImage, MonochromeImage


class IPPrototype(object):
    def __init__(self):
        self._processors = {}

    def processors_list(self):
        return self._processors.keys()

    def add_processor(self, name, proc):
        self._processors[name] = proc

    def delete_processor(self, name):
        del self._processors[name]

    def clone(self):
        return copy.deepcopy(self)


class PrototypeFactory:
    __bia = None
    __mia = None

    @staticmethod
    def initialize():
        PrototypeFactory.__bia = IPPrototype()
        PrototypeFactory.__bia.add_processor('bin_image1', BinaryImage())
        PrototypeFactory.__bia.add_processor('bin_image2', BinaryImage())

        PrototypeFactory.__mia = IPPrototype()
        PrototypeFactory.__mia.add_processor('mono_image', MonochromeImage())

    @staticmethod
    def getBIAPrototype():
        return PrototypeFactory.__bia.clone()

    @staticmethod
    def getMIAPrototype():
        return PrototypeFactory.__mia.clone()


if __name__ == "__main__":
    PrototypeFactory.initialize()

    print(PrototypeFactory.getBIAPrototype().processors_list())
    print(PrototypeFactory.getMIAPrototype().processors_list())
