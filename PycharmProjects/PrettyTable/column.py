from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name", ["Debby", "Bobby", "John", "Joy", "Jake", "Rose", "Mary"])
table.add_column("Gender", ["Female", "Male", "Male", "Female", "Male", "Female", "Female"])
table.add_column("Role", ["Technical Officer", "Auditor", "Accountant", "Manager", "HR", "Secretary", "Store Officer"])
table.add_column("Qualification", ["Bachelors", "Bachelors", "PhD", "Bachelors", "Bachelors", "Masters", "Bachelors"])
table.add_column("Salary", [10000, 15000, 20000, 22000, 24000, 23000, 8500])

print(table)

