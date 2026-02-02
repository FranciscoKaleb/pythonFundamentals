

# Lists is like the all the c++ containers that can contain any data type
# Lists is NOT immutable, you can change its members
# able to contain any datatype unlike c++/Java which only allows specific data type for a container



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
print(num_list[0])
print()



# [4] Performing Arithmetic operation on a list element (if its a number)
print('-----------------[4 Arithmetic Operation]------------------')
print(num_list[1]*5)
print()



# [5] Changing a list element through direct element access
print('-----------------[5 changing a list element]------------------')
num_list[0] = 700
print(num_list)