from dataclasses import dataclass, field
import random
import string



def generate_id():
    return "".join(random.choices(string.ascii_uppercase, k=8))


class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)


    # Post initialize, initiates after an instance has been created
    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"
 

def main() -> None:
    person = Person(name="Dolamu", address="123 California USA")
    print(person)

if __name__ == "__main__ ":
    main()

    

    