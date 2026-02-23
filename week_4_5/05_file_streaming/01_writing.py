

# created outside
print('-----------------[1]------------------')
f = open('readmeey.txt', 'w')  #if file exist, recreates file
f.write("ming ming ming")
f.close()

# created inside week_4_5 folder
print('-----------------[1]------------------')
f = open('week_4_5/readmee.txt', 'w')  #if file exist, recreates file
f.write("ming ming ming")
f.close()

