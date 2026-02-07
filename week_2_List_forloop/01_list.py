
# Python list characteristics:

# Can contain duplicate items
# Mutable: items can be modified, replaced, or removed
# Ordered: maintains the order in which items are added
# Index-based: items are accessed using their position (starting from 0)
# Can store mixed data types (integers, strings, booleans, even other lists)



# [1] Declaring an empty list
print('-----------------[1 Empty List]------------------')
empty_list = []
print(empty_list)
print() # add space



# [2] list that contains numbers 
print('-----------------[2 printing list]------------------')
num_list = [1,2,3,4,5,6,7,8,9,10]
print(num_list)
print()



# [3] accessing list elements
print('-----------------[3 Accessing list elements]------------------')
print(num_list[1])
print()



# [4] Performing Arithmetic operation on a list element (if its a number)
print('-----------------[4 Arithmetic Operation]------------------')
print(num_list[1]*5)
print()



# [5] Changing a list element through direct element access
print('-----------------[5 changing a list element]------------------')
num_list[0] = 700
print(num_list)