programming_dictionary = {
    "Bug": "An error in a program that prevent the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.", 
}

#Retrieving Item from Dictionary - #name_of_dictionary[key]
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

#Adding new value to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A spider in your computer."
print(programming_dictionary)

#Using loops for dictionary
for key in programming_dictionary:  #prints out the keys of the dict
    print(key)
    print(programming_dictionary[key])


