print('-----------------[1 Comparison Operators]------------------')
print(10 == 10)   # Equal to
print(10 != 5)    # Not equal to
print(10 > 5)     # Greater than
print(5 < 10)     # Less than
print(10 >= 10)   # Greater than or equal to
print(5 <= 10)    # Less than or equal to
print('-----------------[2 Comparison with Different Data Types]------------------')
print(10 == 10.1)   # int and float comparison
print('10' == 10)    # str and int comparison
print('a' < 'b')     # str comparison based on ASCII values
print('-----------------[3 Chained Comparisons]------------------')
print(5 < 10 < 15)   # True if 5 < 10 and 10 < 15. Same as (5 < 10) and (10 < 15)
print((5 < 10) and (10 < 15))  # Equivalent to the above 
print('-----------------[4 Comparison Operators with Variables]------------------')
a = 20
b = 15
print(a > b)    # True
print(a == b)   # False
print(a <= b)   # False
