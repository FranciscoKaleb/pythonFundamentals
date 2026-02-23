#[5] using with 'open(filepath) as variable_name:' to automatically close a file
print('-----------------[4]------------------')
with open('readmee.txt', 'r') as f_var:
    print(f_var.read())
print('-----------------[5]------------------')
with open("readmee.txt", 'w') as f_var:
    f_var.writelines('kaleb \nmarquez')
print('-----------------[6]------------------')
with open("readmee.txt", 'r') as f_var:
    tempstring = f_var.read()
    print(tempstring)