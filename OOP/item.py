import csv


class Item:
    pay_rate = 0.8  # Class attribute
    all = []

    def __init__(self, name: str, price: float | int, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    
    @property  #ENCAPSULATION
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price *= self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    

    @property
    # Property Decorator = Read-Only Attribute
    def name(self): # function is now a property
        print("You are trying to get name")
        return self.__name

    @name.setter  #function to change the name property 
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            print("You are trying to set")
            self.__name = value

    def calculate_total_price(self) -> int:
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            # print(reader)
            items = list(reader)
            # print(items)

        for item in items:  # writing the instance of Item again for each item in the list
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        pass
    
    @property
    def read_only_name(self):
        return "AAA"

    def __repr__(self):  # Object representation when print() is activated on object
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def connect(self, smpt_server):
        pass

    def prepare_body(self):
        pass 
    
    def send_email():
        pass
