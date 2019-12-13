import json
# Read json data from json file
fh = open('person.json')
jdata = json.load(fh)
print(type(jdata))
print(jdata)

# Write json data into json file

# person_dict = {'name': 'Sravani','languages': ['Python', 'java'], 'eid': 99, 'age': }

# with open('write_json.txt', 'w') as json_file:
   # json.dump(person_dict, json_file)


''''
error

TypeError: dump() missing 1 required positional argument: 'fp'
'''
