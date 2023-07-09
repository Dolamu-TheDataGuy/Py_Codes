from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Gender", "Role", "Qualification", "Salary"]
table.add_row(["Debby", "Female", "Technical Officer", "Bachelors", 10000])
table.add_row(["Bobby", "Male", "Auditor", "Bachelors", 15000])
table.add_row(["John", "Male", "Accountant", "PhD", 20000])
table.add_row(["Joy", "Female", "Manager", "Bachelors", 22000])
table.add_row(["Jake", "Male", "HR", "Bachelors", 24000])
table.add_row(["Rose", "Female", "Secretary", "Masters", 23000])
table.add_row(["Mary", "Female", "Store Officer", "Bachelors", 8500])

print(table.get_string(sortby="Role"))

