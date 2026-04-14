#Dictionaries is the equivalent of unordered map in c++
#it is unordered and cannot be sorted
#it is a key - value pair, key is always a string
#[1]
print('\n\n')
print('-----------------[1 basic printing]------------------')
dictionary1 = {
        'key1':'value1',
        'key2': 3,
        'key3': {
                '1': [1,2,3],
                '2': [1,2,3]
            },
    }
# print(dictionary1)
print(dictionary1['key3']['1']) #accessing value using key
print('\n\n')

print('-----------------[2 basic]------------------')
dictionary2 = {'kaleb':26,'Sam':20}
print(dictionary2)
print(dictionary2['kaleb'])

print('\n\n')

print('-----------------[3 for loop]------------------')
dictionary2 = {
    'kaleb':26,
    'Sam':20,
    'John':30,
    'Mary':25
}

for key in dictionary2:
    print(f'{key} {dictionary2[key]}') #prints keys only


print('\n\n')

print('-----------------[4 adding pair]------------------')
dictionary2['Jane'] = 22 #adding a pair to the dictionary
for key in dictionary2:
    print(f'{key} {dictionary2[key]}') #prints keys only


print('\n\n')

print('-----------------[5 key uniqueness]------------------')
dictionary2['Jane'] = 29 #if we add a pair with the same key, it will update the value of that key but not add a new pair
for key in dictionary2:
    print(f'{key} {dictionary2[key]}') #prints keys only


print('\n\n')