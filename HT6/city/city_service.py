

class CityService:
    def __init__(self, name, max_cities):
        self._name = name
        self._max_cities = max_cities
        self._cities = list()

    def remove_person(self, person_name, person_surname, person_middle_name, city_name):
        for city in self._cities:
            if city.get_name() == city_name:
                for p in city.get_persons():
                    if p.get_name() == person_name and p.get_surname() == person_surname and p.get_middle_name() == person_middle_name:
                        city.remove_person(p)
        return False

    def add_person(self, person, city_name):
        for city in self._cities:
            if city.get_name() == city_name:
                return city.add_person(person)
        return False

    def remove_family(self, family_name, city_name):
        for city in self._cities:
            if city.get_name() == city_name:
                for family in city.get_families():
                    if family.get_name() == family_name:
                        return city.remove_family(family)
        return False

    def add_family(self, family, city_name):
        for city in self._cities:
            if city.get_name() == city_name:
                return city.add_family(family)
        return False

    def remove_city(self, city_name):
        for city in self._cities:
            if city.get_name() == city_name:
                self._cities.remove(city)
        return False

    def add_city(self, newCity):
        if self._max_cities <= len(self._cities):
            return False

        for city in self._cities:
            if city.get_name() == newCity.get_name():
                return False
        self._cities.append(newCity)
        return True

    def add_person_to_family(self, child, surname):
        for city in self._cities:
            for family in city.get_families():
                if family.get_name() == surname:
                    return city.add_children(child)
        return False

    def count_citizens(self):
        count = 0
        for index in range(len(self._cities)):
            count += len(self._cities[index].get_residents())
        return count

    def count_families(self):
        count = 0
        for index in range(len(self._cities)):
            count += len(self._cities[index].get_families())
        return count

    def __str__(self):
        s = []
        s.append("------------------------ \n")
        s.append("CityService: \n")
        s.append("Name: {}\n".format(self._name))
        s.append("Cities: {}\n".format(len(self._cities)))
        s.append("Citizens: {}\n".format(self.count_citizens()))
        s.append("Families: {}\n".format(self.count_families()))
        s.append("------------------------ \n")

        return ''.join(s)
