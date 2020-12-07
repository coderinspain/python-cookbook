d = {'pet': 'dog', 'age': 5, 'name': 'spot'}
# print(d)

# print(f'Items: {d.items()}')
# print(f'Keys: {d.keys()}')
# print(f'Values: {d.values()}')

# Getting a value from the key
# print(f'Name: {d["name"]}')
# print(f'Test: {d["bla"]}') #Throw an error if the key is not found

# Add an item
d['trick'] = 'sit'
print(d)
d['trick'] = 'rollover' # Keys are inmutable can not be changed! You have to delete and create a new one
print(d)

# Removing a item
del d['trick']
print(d)

#Testing for existence 
if 'name' in d:
    print(d['name'])

#Looping 
for key in d.keys():
    print(f'{key} = {d[key]}')