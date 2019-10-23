class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion('wangi')
print(lion)

class Lion:
    def __init__(self, name):
        self.name = name

lion2 = Lion('LEE')
print(lion2.name)