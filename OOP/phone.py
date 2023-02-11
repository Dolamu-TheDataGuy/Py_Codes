from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float | int, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        # Run validation to the received arguments
        assert broken_phones >= 0, f"Broken phones {quantity} is not greater or equal to zero"
        # Assign to self object
       
        self. broken_phones = broken_phones
        
if __name__ == "__main__":
    phone1 = Phone("jscPhonev10", 500, 5, 1)
    print(Item.all)
    print(Phone.all)