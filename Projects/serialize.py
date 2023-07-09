import json
#Serializing 
passport = {"name": "John", "last name": "Doe", "titles" : [
    "Servant of the Secret Flame", 
    "Elf-friend"]}

with open("passport.json", "w") as file:
    json.dump(passport, file)

json_string = json.dumps(passport)
print(json_string)

with open("passport.json", "w") as file:
    file.write(json_string)

#Deserializing
json_string = '{"name": "Jane", "last name": "Doe", "titles":["Head of the White Council"]}'
data = json.loads(json_string)
print(data)

#YAML
import yaml
items = {
    "Wizard staff": 1,
    "Mithril chain mail": 1,
    "Elven bread": 5,
    "Magic rings: " : ["Ring of Adamant", "Ring of Sapphire"]
}

character = {
    "personal information": passport,
    "inventory": items
}

with open("character.yaml", "w") as file:
    yaml.dump(character, file)

#Pickle
import pickle

with open("data.pkl", "wb") as file:
    pickle.dump(items, file)

with open("data.pkl", "rb") as file:
    new_data = pickle.load(file)

print(new_data)