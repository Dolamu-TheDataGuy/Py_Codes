class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


person = Person("John", 13)
person.name = "Adam"
print(person.name)