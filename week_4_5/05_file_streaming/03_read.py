#[3] READ A FILE
print('-----------------[3]------------------')
f = open('readmee.txt', 'r')  
temp = f.read()
print(temp)
f.close()
