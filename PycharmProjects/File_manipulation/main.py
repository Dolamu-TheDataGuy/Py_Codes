file = open("/Users/Dolzy/Desktop/my_file.txt")  # Absolute path
contents = file.read()
print(contents)
file.close()

with open("../../Desktop/my_file.txt", "r") as f:  # Automatically closes tthe file
    app = f.read()
    print(app)

with open("../../Desktop/new_file.txt", "w") as f:  # Relative path
    f.write("Apache Programming language is cool.")
