try:
    file = open("a.txt")
    a = {"key": "value"}
    print(a["iadd"])
except FileNotFoundError:
    file = open("a.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error I made up")

