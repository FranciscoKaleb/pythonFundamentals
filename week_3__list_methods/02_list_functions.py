



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
print(sorted(myList5))
print(myList5)



data = [
    ['kaleb', 300],
    ['kaleb', 900],
    ['sam', 800]
]

price_list = [x[1] for x in data]
print(price_list)