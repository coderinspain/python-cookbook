# jason_files

import json

filename = 'json.txt'

#To string
outD = dict(name='Mario', age='47', pet='Horse')
s = json.dumps(outD) #Dumps put it to a string
print(f'String={s}')

#To file
with open(filename, 'w') as f:
    json.dump(outD, f) #Dump puts it to a file

#From string
inD = json.loads(s) # Load the dictionary from the string
print(f'Dictionary = {inD}')

#From file
with open(filename, 'r') as f:
    p =json.load(f)
print(f'Type: {type(p)} = {p}')



