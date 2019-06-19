dict = {'Name': 'Zara','Age': 7,'Class': "First"}


print(dict['Name'])

print(dict)
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print(dict)


del dict['Name'] # remove entry with key 'Name'
print(dict)
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

print(dict)
