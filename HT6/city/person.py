class Person:
    def __init__(self, _name, _surname, _midname):
        self._name = _name
        self._surname = _surname
        self._middle_name = _midname

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_middle_name(self):
        return self._middle_name

    def __str__(self):
        return "{} {} {}".format(self._name, self._surname, self._middle_name)

    def __del__(self):
        pass
