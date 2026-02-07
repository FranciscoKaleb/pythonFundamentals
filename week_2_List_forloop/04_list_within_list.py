


# name, age, gender, finished college
data = [
    ['Kaleb', 29, 'Male', True],
    ['Francisco', 35, 'Male', False],
    ['John', 20, 'Male', False],
    ['Sam', 22, 'Female', True],
    ['May', 26, 'Female', True],
]


# 10 Accessing a list within a list
print('-----------------[10 list within list]------------------')
print(data[0])
print()


# 10 Accessing the element of a list within list
print('-----------------[11 accessing element of a list within list]------------------')
print(data[0][0])
print(data[0][1])
print(data[0][2])
print(data[0][3])
# print(data[0][4]) #will cause error
print()


# 11 printing each 'row'
print('-----------------[12 printing each row]------------------')
for mem in data:
    print(mem)

print()


# 12 print only a specific column. name 
print('-----------------[13 printing a specific column]------------------')
for mem in data:
    print(mem[0])

print()


# 13 Perform arithmetic operation on a specific column
print('-----------------[13 print sum of ages and get average]------------------')
# lets say sum of ages
age_sum = 0
age_average = 0

for mem in data:
    age_sum = age_sum + mem[1]
    
age_average = age_sum/len(data)
print(f'sum: {age_sum}')
print(f'Average: {age_average:.2f}') # we added :.2f to have cleaner format, 2 decimal place rounded off



# 14 print only below age 25
print('-----------------[14 Using if else]------------------')
for mem in data:
    if mem[1] > 25:
        print(mem)
    else:
        pass



# 15 Print those above 25 and finished college
print('-----------------[15 for loop and conditions]------------------')
for mem in data:
    if mem[1] > 25 and mem[3] == True:
        print(mem)
    
print()
    
# 16 get the average age of above 25 and finished college
print('-----------------[15 for loop and conditions]------------------')
age_average = 0
aa_25_t_sum = 0
aa_25_t_count = 0

for mem in data:
    if mem[1] > 25 and mem[3] == True:
        aa_25_t_sum = aa_25_t_sum + mem[1]
        aa_25_t_count = aa_25_t_count + 1

age_average = aa_25_t_sum/aa_25_t_count
print(f'Average age of age greater then 25 and finished college: {age_average}')








# total sales:  Summation of price x quantity sold

# average price per category:
# (sum of price of a category) / (count_of_category)






