print('-----------------[1 If Statements]------------------') 
if 10 > 5:
    print("10 is greater than 5")
    print("10 is greater than 5")
    
print('-----------------[2 If-Else Statements]------------------')

if 10 > 5:
    print("10 is less than 5")


print('-----------------[3 If-Elif-Else Statements]------------------')

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
    
    
print('-----------------[4 Nested If Statements]------------------')
num = 15
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else: 
        print("The number is positive and odd.") 
     
        
print('-----------------[5 multiple If Statements]------------------')
num = 6
if num > 0:
    print("The number is positive.")
if num % 2 == 0:
    print("The number is even.")