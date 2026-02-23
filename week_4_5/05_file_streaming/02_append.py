#[2] APPEND mode doesnt recreate the file
print('-----------------[2]------------------')
f = open('readmee.txt', 'a')  
f.write("\n\ncute dog")
f.close()