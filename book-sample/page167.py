class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name


mike = Person('Mike wangi')
dog = Dog('happy', 'bulldog', mike)

print(dog.owner.name)
print(dog.name)