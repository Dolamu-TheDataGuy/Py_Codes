import json


# creating the json file
data = {
	"name": "Satyam kumar",
	"place": "patna",
	"skills": [
		"Raspberry pi",
		"Machine Learning",
		"Web Development"
	],
	"email": "xyz@gmail.com",
	"projects": [
		"Python Data Mining",
		"Python Data Science"
	]
}
with open( "data_file.json" , "w" ) as write:
	json.dump( data , write, indent=4)



# Using the load method to read the json file to console
with open("data_file.json", "r") as read_content:
	print(json.load(read_content))