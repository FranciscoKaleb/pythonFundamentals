

# to use local variable inside the function, we need to declare it as global inside that function
num = 5

def addtwo():
    global num
    num = num + 2
    
addtwo()
print(num)