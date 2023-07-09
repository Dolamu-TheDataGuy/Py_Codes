fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError: # what happens when the error is caught
        print("Fruit pie")
    else:  # What happens when the code in the try block runs
        print(fruit + " " + "pie")


make_pie(2)
