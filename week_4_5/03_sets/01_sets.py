#Sets are unordered collection of UNIQUE elements
# UNIQUE - no duplicates

mySet = set()


print(mySet)
mySet.add(1)
print(mySet)
mySet.add(2)
print(mySet)
mySet.add(2) #ignored - not added in mySet
print(mySet)
mySet.add('kaleb')
print(mySet)

print('-------------[1]--------------')
myList = [1,2,3,3,3,3,3,4,4,4,4,55,5]
mySet = set(myList) #turn list into set using casting type, deletes duplicates of 3 and 4
print(mySet) 

print('-------------[2]--------------')
myString = 'mississippi'
print(set(myString)) #deletes repeating letters



