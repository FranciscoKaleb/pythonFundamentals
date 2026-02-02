print('-----------------[1 Logical Operators]------------------')
print(True and False)   # Logical AND 
print(True or False)    # Logical OR
print(not True)         # Logical NOT
print('-----------------[2 Logical Operators with Comparison]------------------')
print((10 > 5) and (5 < 3))   # True and False
print((10 == 10) or (5 != 5)) # True or False
print(not(10 <= 5))         # not False
print('-----------------[3 Logical Operators with Variables]------------------')
a = 10
b = 5
print((a > b) and (b < 3))   # True and False
print((a == 10) or (b != 5)) # True or False
print(not(a <= b))         # not False
print('-----------------[4 Short-Circuit Evaluation]------------------')
# In 'and', if the first operand is False, the second is not evaluated
print(False and (10 / 0 > 1))  # Does not raise an error

# In 'or', if the first operand is True, the second is not evaluated
print(True or (10 / 0 > 1))   # Does not raise an error

