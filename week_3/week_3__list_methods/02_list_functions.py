



# len(a)
print('-----------------[1] len(a)]------------------')
myList = [1, 2, 3, 4, 5]
print(len(myList))
print()
# sum(a)
print('-----------------[2] sum(a)]------------------')
myList2 = [1, 2, 3, 4, 5]
print(sum(myList2))
print()
# max(a)
print('-----------------[3] max(a)]------------------')
myList3 = [1, 2, 3, 4, 5]
print(max(myList3))
print()

# min(a)
print('-----------------[4] min(a)]------------------')
myList4 = [1, 2, 3, 4, 5]
print(min(myList4))
print()

# sorted(a)
print('-----------------[5] sorted(a)]------------------')
myList5 = [5, 4, 3, 2, 1]
newlist = sorted(myList5)
print(newlist)
print(myList5)


data = [
    ['kaleb', 300,3],
    ['kaleb', 900,5],
    ['sam', 800,9]
]
print(max([x[1] for x in data]))
