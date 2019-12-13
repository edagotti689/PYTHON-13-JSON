'''
1. JSON stands for JavaScript Object Notation
2. JSON is a lightweight format for storing and transporting data
3. A name/value pair consists of a field name in double quotes("Name":"Sriram")
'''

import json

# create json data
# p = '{"name": "sri", "languages": ["Python", "Java"]}'

# convert json to python dictionary
# person_dict = json.loads(p)
# print(type(person_dict), person_dict)


# convert dictionary to json
d = {'name':'sri', 'eid':456}
j = json.dumps(d)
# print(type(j))
print(j)


