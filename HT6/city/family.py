class Family:
    def __init__(self, wife, husband):
        self._surname = husband.get_surname()
        self._wife = wife
        self._husband = husband
        self._children = list()

    def count(self):
        return 2 + len(self._children)

    def get_members(self):
        members = [self._wife, self._husband]

        for child in self._children:
            members.append(child)

        return members

    def get_name(self):
        return self._surname

    def add_children(self, children):
        self._children.append(children)

    def remove_children(self, children):
        self._children.remove(children)

    def __str__(self):
        s = []
        s.append("------------------------ \n")
        s.append("Family: \n")
        s.append("Name: {}\n".format(self._surname))
        s.append("W: {}\n".format(self._wife))
        s.append("H: {}\n".format(self._husband))
        s.append("Children:\n")
        for c in self._children:
            s.append("{}\n".format(c))
        s.append("------------------------ \n")

        return ''.join(s)

    def __del__(self):
        pass
