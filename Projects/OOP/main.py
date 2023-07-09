from item import Item
from phone import Phone


if __name__ == "__main__":
    Item.instantiate_from_csv()

    print(Item.all)