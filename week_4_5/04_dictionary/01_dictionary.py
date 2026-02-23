#Dictionaries is the equivalent of unordered map in c++
#it is unordered and cannot be sorted
#it is a key - value pair, key is always a string
#[1]
dictionary1 = {'key1':'value1','key2':'value2'}
dictionary2 = {'kaleb':26,'Sam':20}
dictionary3 = {'Apple':25,'Orange':15, 'Banana':10}
dictionary4 = {'k1': 23, 'k2':[1,2,3], 'k3':{'secondlayer':{'thirdlayer':100}}}
dictionary5 = {'key':['a', 'b', 'c']}

print('-----------------[1]------------------')
print(dictionary2['kaleb']) #prints 26
print(dictionary3['Banana'])
print(dictionary4.keys())
print(dictionary4['k3'])
print(dictionary4['k3'])
print(dictionary4['k3']['secondlayer'])
print(dictionary4['k3']['secondlayer']['thirdlayer'])
print(dictionary5['key'][0].upper())
print(dictionary5)
# adding new pair to a dictionary
dictionary1['key3'] = 'value3'
print(dictionary1['key3'])

#[2]reassigning values
print('-----------------[2]------------------')
dictionary5['key'][0] = dictionary5['key'][0].upper()
print(dictionary5)
dictionary2['kaleb'] = 27
print(dictionary2)
dictionary2['kaleb'] = 'string1'
print(dictionary2)

#[3]printing keys and values
print('-----------------[3]------------------')
print(dictionary3.keys())
print(dictionary3.values())
print(dictionary3.items()) # returns a tuple



