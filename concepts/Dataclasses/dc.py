from dataclasses import dataclass

@dataclass 
class Person:
    name: str
    job: str
    age: int


person1 = Person("Seun", "Witcher", 30)
person2 = Person("Yenner", "Craft", 25)
person3 = Person("Yenner", "Craft", 25)

print(id(person2))
print(id(person3))
print(person1.name)
print(person2 == person3) #Result becomes true on using dataclass because they contain the same data