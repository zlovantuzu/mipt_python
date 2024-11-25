from person import Person
from city import City
from family import Family
from city_service import CityService


def person_test():
    p = Person('a', 'b', 'c')
    print(p)

    p2 = Person('a2', 'b2', 'c2')
    print(p2)


def city_test():
    c1 = City("City1", 10)
    p = Person('a', 'b', 'c')
    c1.add_person(p)
    print(c1)

    c2 = City("City2", 15)
    print(c2)

    for i in range(18):
        p2 = Person('a{}'.format(i), 'b{}'.format(i), 'c{}'.format(i))
        if not c2.add_person(p2):
            print("not enough space in city")
    print(c2)


def family_test():
    c1 = City("City1", 10)
    w = Person("Wife", "test", "first")
    h = Person("Husband", "test", "first")
    f1 = Family(w, h)
    print(f1)
    c1.add_family(f1)
    print(c1)

    w2 = Person("Wife2", "test2", "first")
    h2 = Person("Husband2", "test2", "first")
    f2 = Family(w2, h2)

    c2 = Person("child2", "test2", "first")
    f2.add_children(c2)
    c3 = Person("child3", "test2", "first")
    f2.add_children(c3)
    print(f2)

    c2 = City("City2", 10)
    c2.add_family(f2)
    print(c2)


def service_test():
    c1 = City("City1", 10)
    w = Person("Wife", "test", "first")
    h = Person("Husband", "test", "first")
    f1 = Family(w, h)

    cs = CityService("city_service1", 20)

    cs.add_city(c1)
    cs.add_family(f1, c1.get_name())

    c1 = Person("child1", "test", "first")
    c2 = Person("child2", "test", "first")

    cs.add_person_to_family(c1, c1.get_surname())
    cs.add_person_to_family(c2, c2.get_surname())

    print("test1")
    print(cs)

    w2 = Person("Wife2", "test2", "first")
    h2 = Person("Husband2", "test2", "first")
    f2 = Family(w2, h2)

    c2 = City("City2", 15)
    cs.add_city(c2)
    cs.add_family(f2, c2.get_name())

    for i in range(4):
        c = Person("child2{}".format(i), "test2", "Husband2")
        cs.add_person_to_family(c, c.get_surname())

    print("test2")
    print(cs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Program is started")

    # person_test()
    # city_test()
    # family_test()
    service_test()

    print("Program is finished")
