



# [7] for each loop - using for each loop to iterate through list elements
print('-----------------[7 printing list using for in loop / for each loop]------------------')
num_list = [1,2,3,4,5,6,7]

for mem in num_list:
    print(mem)



# [8] Performing Arithmetic operation for each list members
# lets say we multiply each member of the list by 2
print('-----------------[8 Arithmetic Operation on each element]------------------')

for mem in num_list:
    print(mem*2)
    
    

# [9] getting the sum of the num list
print('-----------------[9 sum of list]------------------')
sum = 0
for mem in num_list:
    sum = sum + mem

print(f'sum: {sum}')


