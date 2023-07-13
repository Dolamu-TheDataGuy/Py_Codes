from dataclasses import dataclass, field

@dataclass 
class Person:
    sort_index:int= field(init=False)
    name: str
    job: str
    age: int

    def __post_init__(self):
        self.sort_index = self.age


person1 = Person("Seun", "Witcher", 30)
person2 = Person("Yenner", "Craft", 25)
person3 = Person("Yenner", "Craft", 25)

print(id(person2))
print(id(person3))
print(person1.name)
print(person2 == person3) #Result becomes true on using dataclass because they contain the same data