# List comprehension offers a shorter syntax when you want to create a new list 
# based on the values of an existing list.

#[1] creating an empty list with specific index
print('-----------------[1]------------------')
myList = [None] * 5
print(myList)

#[2] appending strings to a list using for loop
print('-----------------[2]------------------')
myList2 = []
myString = 'Hello world'

for mem in myString:
    myList2.append(mem)

print(myList2)

#another method through conversion using list()
new_list = list(myString)
print(new_list)

#[3] list comprehension
print('-----------------[3]------------------')
myList3 = [x for x in 'Helo world']

print(myList3)

#[4] using range()
print('-----------------[4]------------------')
myList4 = [num**2 for num in range(0,20)]

print(myList4)

#[5] grabbing only even number using if
print('-----------------[5]------------------')
myList5 = [x for x in range(0, 21) if x%2 == 0]
print(myList5)

#[6] celcius example
print('-----------------[6]------------------')
celcius = [0, 20, 20, 34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]

print(f' celcius = {celcius}')
print(f' fahrenheit = {fahrenheit}')

#[7] using if else inside list comprehension
print('-----------------[7]------------------')
result = [x if x%2 == 0 else 'ODD' for x in range(0, 21)]

print(result)

#[8] multiplying list and appending result in a new list using nested for loop\
print('-----------------[8]------------------')
myList6 = []
for x in [1,2,3]:
    for y in [100, 200, 300]:
        myList6.append(x*y)
print(myList6)

#[9] nested for loop in list comprehension(for loop inside a for loop) - 
print('-----------------[9]------------------')
myList7 = [x*y for x in [1,2,3] for y in [100,200,300]]
print(myList7)





