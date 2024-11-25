from person import Person


class City:
    __max_count = 100

    def __init__(self, name, max_count):
        self._name = name
        self._max_count = max_count
        self._residents = list()
        self._families = list()

    def get_name(self):
        return self._name

    def add_family(self, family):
        if self.__max_count - len(self.get_residents()) > family.count():
            self._families.append(family)
            return True
        return False

    def remove_family(self, family):
        if self.__max_count - len(self.get_residents()) > family.count():
            self._families.remove(family)
            return True
        return False

    def get_residents(self):
        members = list()
        for i in range(len(self._families)):
            for m in self._families[i].get_members():
                members.append(m)

        for i in range(len(self._residents)):
            members.append(self._residents[i])
        return members

    def get_families(self):
        return self._families

    def get_persons(self):
        return self.get_residents()

    def add_person(self, person):
        if len(self.get_residents()) < self._max_count:
            self._residents.append(person)
            return True
        return False

    def remove_person(self, person):
        if len(self._residents) > 0:
            self._residents.remove(person)
            return True
        return False

    def __str__(self):
        s = []
        s.append("------------------------ \n")
        s.append("City: \n")
        s.append("Name: {}\n".format(self._name))
        s.append("Max_person_count: {}\n".format(self._max_count))
        s.append("Cur_count: {}\n".format(len(self.get_residents())))
        s.append("Free: {}\n".format(self._max_count - len(self.get_residents())))
        s.append("------------------------ \n")

        return ''.join(s)
