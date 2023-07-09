from prettytable import PrettyTable
table = PrettyTable()   # make an object

# invoke a method
table.add_column("City name",
["Adelaide", "Brisbane", "Darwin", "Horbart", "Sydney", "Melbourne"])

table.add_column("Area", [1000, 45600, 6000, 5000, 300, 2000])
table.add_column("Type", ["Electric", "Water", "Fire", "Water", "Electric", "Weather"])
table.align = "l"


print(table)

