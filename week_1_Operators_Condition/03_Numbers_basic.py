# Addition, subtraction, multiplication, division
print('-----------------[1]------------------')
print(1+1) 
print(1-2)
print(2*3)
print(20/4)

#modulo/ get the remainder
print('-----------------[2]------------------')
print(10%7)


print('-----------------[3 type conversion - Implicit ]------------------')
# In implicit conversion, the Python interpreter automatically converts one data type to another to avoid data loss.
result = 5 + 2.1 # int 5 is implicitly converted to float 5.0
print(result)  # Output: 7.0

print('-----------------[3 type conversion - Explicit ]------------------')
# In explicit conversion, the programmer manually converts one data type to another.
num_str = "123" 
num_int = int(num_str)  # Convert string to integer
print(num_str)  # Output: 123

