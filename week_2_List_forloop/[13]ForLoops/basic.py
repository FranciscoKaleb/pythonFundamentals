#used for iterating in a container such as Lists, dictionaries, tuple, sets or string

#[1] For loop basic, printing Lists elements
print('-----------------[1]------------------')
myList = [1,2,'dog']
for mem in myList:
    print(mem)

#[2] printing 'hello' every iteration 
myList2 = [1,2,3,4,5,6,7,8,9,0]
print('-----------------[2]------------------')
for mem in myList2:
    print('hello')

#[3] printing only even numbers, by using if statement inside a for loop
print('-----------------[3]------------------')
for mem in myList2:
    if mem%2 == 0:
        print (f'{mem} is even')
    else:
        print(f'{mem} is odd')

#[4] adding up all the numbers in the list, accumulate
print('-----------------[4]------------------')
myList2_sum = 0
for mem in myList2:
    print(f'{myList2_sum} + {mem} = {myList2_sum + mem}')
    myList2_sum = myList2_sum + mem
print(myList2_sum)
































#[5] looping through a tuple
print('-----------------[5]------------------')
myTuple = (1,2,3,3)
for mem in myTuple:
    if mem == 2:
        mem = 3
    print(mem)
print(myTuple) # mem is a copy

#[6] tuple unpacking
print('-----------------[6]------------------')
myTupleList = [(1,2), (3,4), (5,6), (7,8), (9,10)] #tuple pairs inside a lists
for mem in myTupleList:
    print(mem)

for (a,b) in myTupleList:
    print(a)
    print(b)

#[7] dictionary, printing values/keys in a key value pair
print('-----------------[7]------------------')
myD = {'k1':'P001', 'k2':'P002', 'k3':'P003'}
for mem in myD.keys(): # or myD.values()
    print(f'{mem} : {myD[mem]}')



        