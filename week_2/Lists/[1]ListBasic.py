
# Lists is like the all the c++ containers that can contain any data type
# Lists is NOT immutable, you can change its members
# able to contain any datatype unlike c++ which only allows specific data type for a container

#[1] basic - putting values, accessing index
print('-----------------[1]------------------')
myList = [1,2,13,4,15,6,7,7,8,9,0]
myList2 = ['String', 100, 23.2]
myList3 = ['one', 'two', 'three']
myList4 = ['five', 'six', 'seven']
lettersList = ['t', 'b', 'c', 's', ]
arr 
print(len(myList2)) # outputs 3
print(myList3[0])
print(myList[1:])

#[2] concatenating list using '+'
print('-----------------[2]------------------')
myList5 = myList4 + myList3
print(myList5) 

#[3] changing elements through direct element access - list_name[index]
print('-----------------[3]------------------')
myList3[0] = 'ONE'
print(myList3)

#[4] append() -- adding elements in the end using append()
print('-----------------[4]------------------')
myList.append(4)
print(myList)

#[5] pop() -- removing items from the BACK of the list using pop()
print('-----------------[5]------------------')
myList.pop()
print(myList)

#[6] saving popped items
print('-----------------[6]------------------')
pop_list = myList.pop()
pop_list = pop_list + myList.pop() # doesnt result into another list but rather an integer
print(f'pop list = {pop_list}')
print(myList)

#[7] pop(index) -- removing items in any index using pop(index)
print('-----------------[7]------------------')
myList5.pop(1)
print(f'myList5 -- > {myList5}')
print(f'using pop(index) on myList5 {myList5}')
print('note that seven is deleted/removed from myList5')

#[8] sort() ascending --  has NO return type - sorts the actual list
print('-----------------[8]------------------')
myList.sort()
print(myList)

#[9] will not work because .sort() does not return a type 
print('-----------------[9]------------------')
newList = myList.sort()
print(newList)
print(f'type of newList is {type(newList)}')
#will work
newList = myList
print(newList)

#[10] reverse() descending -- reverse sort
print('-----------------[10]------------------')
newList.reverse()
print(newList)

#[11] insert(index, value) - insert a value to an index, moves the original value one index up
print('-----------------[11]------------------')
print(myList)
myList.insert(3,444)
print(myList)

#[12] copy() - copying a list
print('-----------------[12]------------------')
myList6 = [1,2,3,4,5,6]

myList6Copy = myList6

print(myList6)
print(myList6Copy)

myList6Copy[1] = 444 #change the myList6 as well

print(myList6)
print(myList6Copy)

myList6Copy = myList6.copy()

print(myList6)
print(myList6Copy)

myList6Copy[1] = 445 #change the myList6 as well

print(myList6)
print(myList6Copy)

#[13] count()
print('-----------------[13]------------------')
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x)










