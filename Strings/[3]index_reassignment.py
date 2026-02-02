name = "kaleb" 
# name[0] = 'J' ---> doesnt work like C,C++,C# or java
#python strings are immutable, so you need to create another temp string

#[1] Changing the first letter
print('-----------------[1]------------------')
tempString = 'J' + name[:3]
name = tempString

print(tempString)
print(name)

#[2]Changing letters between
print('-----------------[2]------------------')
tempString = name[:2] + 'r' + name[3:]
print(tempString)

#[3]turning strings into list of letters by casting, then reassignning value to the index of the list
print('-----------------[3]------------------')
nameStr = 'kaleb'
myList = list(nameStr)
#nameStr[2] = 'b' ---> this would cause error

print(f'{nameStr} is the original string')
print(f'{myList} is the list')

myList[2] = 'b'

print(f'{myList} is the result after changing an index value')

nameStr = ''
for mem in myList:
    nameStr = nameStr + mem

print(f'{nameStr} is the result after turning the list into a string')
print("")









