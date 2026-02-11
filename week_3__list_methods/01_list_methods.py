


# [1] concatenating/combining list
print('-----------------[1 concatenating list]------------------')
num_list = [1,2,3,4,5]
num_list2 = [6,7,8,9,10]
print(f'num_list: {num_list}')
print(f'num_list2: {num_list2}')

num_list3 = num_list + num_list2
print(f'num_list3: {num_list3}')
print()



# [2] append() - adding new elements on the end of the list
print('-----------------[2 append()]------------------')
name_list = ['john', 'sam']
print(f'name_list: {name_list}')
name_list.append('jaz')
print(f'name_list: {name_list}')
print()



# [3] pop() - remove the last element of the list
print('-----------------[3 pop()]------------------')
print(f'name_list: {name_list}')
name_list.pop()
print(f'name_list: {name_list}')
print()




# [4] pop(index_num) - remove element of specific index
print('-----------------[4 pop(index_num)]------------------')
car_list = ['honda', 'ford', 'rusi']
print(f'carlist: {car_list}')
car_list.pop(1)
print(f'carlist: {car_list} <--- ford is removed after car_list.pop(1)')
print()




# [5] sort() - ascending --  has NO return type - SORTS THE ACTUAL LIST!!!
print('-----------------[5 sort() - ascending]------------------')
rand_num_list = [99, 77, 43, 68, 92, 2, 1, 14]
rand_num_list.sort()
print(rand_num_list)
print()


# [6] sort(reverse=True) - descending --  has NO return type - SORTS THE ACTUAL LIST!!!
print('-----------------[6 sort(reverse=True) - descending]------------------')
rand_num_list = [99, 77, 43, 68, 92, 2, 1, 14]
rand_num_list.sort(reverse = True)
print(rand_num_list)
print()



# [7] sort(key) - ascending --  has NO return type - SORTS THE ACTUAL LIST!!!
print('-----------------[7 sort(key) - ascending]------------------')
data = [
    [3, 'zhicken', 150],
    [1, 'Pork', 220],
    [2, 'Fish', 180],
]

data.sort(key=lambda x: x[2]) # sort base on index 2 (price)

for row in data:
    print(row)
print()



# [8] sort(key) - descending --  has NO return type - SORTS THE ACTUAL LIST!!!
print('-----------------[8 sort(reverse = True, key) - descending]------------------')
data = [
    [3, 'zhicken', 150],
    [1, 'Pork', 220],
    [2, 'Fish', 180],
]

data.sort(reverse = True, key=lambda x: x[2]) # sort base on index 2 (price)

for row in data:
    print(row)
print()





# [9] reverse() - reverses the list
# this is not sorting
print('-----------------[9 reverse()]------------------')
rand_num_list2 = [99, 77, 43, 68, 92, 2, 1, 14]
rand_num_list2.reverse()
print(rand_num_list2)
print()




# [10] insert(index, value) - 
print('-----------------[10 insert(index, value)]------------------')
num_list = [1,2,3,4,5]
print(num_list)
num_list.insert(1, 555)
print(num_list)
print()




# [11] copy()
print('-----------------[11 copy()]------------------')
new_list = num_list.copy()
print(new_list)
print()




# [12] count()
print('-----------------[12 count()]------------------')
num_list = [1,1,1,1,2,3,4,5]
print(num_list)
print(f'there is/are {num_list.count(1)} number 1 inside the list')
print()