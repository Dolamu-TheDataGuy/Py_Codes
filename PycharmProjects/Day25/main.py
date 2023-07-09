# with open("weather_data.csv", "r") as data_file:
#    data = data_file.readlines()
#    print(data)

import csv

with open("weather_data.csv") as data_file:  # too monotonous, why not use Pandas?
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data_new = pandas.read_csv("weather_data.csv")
# print(type(data_new))
# print(data_new.shape)
# print(data_new['temp'])

# print(data_new.to_dict())

temp_list = data_new["temp"].to_list()
# print(len(temp_list))

# Get Data in Columns
# print(data_new["condition"])
# print(data_new.condition)

# Get Data in Row
# var = data_new[data_new["day"] == "Monday"]
# print(int(var['temp']))

# Create a dataframe from scratch
data_dict = {
    "students": ['Amy', 'James', 'John'],
    "scores": [98, 86, 90]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
