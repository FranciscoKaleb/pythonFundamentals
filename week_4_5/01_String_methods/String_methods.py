
# methods

#[1] upper() - turns all letters in string to upper case
print('-----------------[1 - upper() ]------------------')
x = "Hello World"
print(x.upper()) # doesnt change x, has a return value so it needs assignment '='
print(x)
x = x.upper()
print(x)

#[2] lower() or casefold() - turns letters to lower case; 
print('-----------------[2 - lower() ]------------------')
x = x.lower()
print(x)
x = "ßHi this is a string"
print(x)
x = x.casefold() #converts 'ß' to 'ss'
print(x)

#[3] split() returns list, a data type which is like an equivalent of a container in c++
#[3] partition() is like split but it returns a tuple and split only at first occurence
print('-----------------[3 - split() ]------------------')
x = x.split() # split on white space by default, removes white space
              # x is now a list after split
print(x)

#[4] changing matched word in a string method 1
# has its own specific uses like for example you want to change all the 'an' word in a sentence without affecting
# those words with 'an' in their parts like the word animal, ban, man, tan etc...
# only affecting the 'an' in the phrase 'an apple'
print('-----------------[4 - ]------------------')
myStr2 = 'The dog in the doghood is my friend.\n'\
         'My neighbor always feed the dog with snaks'
print(myStr2)

tempList = myStr2.split() #deletes backslash characters and splits by space
print(tempList)

index_count = 0

while index_count < len(tempList):
    if tempList[index_count] == 'dog':
        tempList[index_count] = 'cat'
    else:
        pass
    index_count += 1

print(tempList)

myStr2 = ''
for mem in tempList:
    myStr2 = myStr2 + mem + ' '

print(myStr2)

#[5] replace() changing matched word in a string using replace() method 2
print('-----------------[5 - replace() ]------------------')
myStr2 = 'The dogin the neighborhood is my friend.\n'\
         'My neighbor always feed the dog with snaks'

myStr3 = myStr2.replace('dog', 'alligator')
print(myStr3)

#[6] split between \n 
print('-----------------[6 - split() ]------------------')

newList = myStr2.split('\n')
print(newList)

#[7] count() counting the occurence of a substring/letter count('substr', start, end)
print('-----------------[7 - count() ]------------------')
myStr2 = 'The dogin the neighborhood is my friend.\n'\
         'My neighbor always feed the dog with snaks'

print(myStr2.count('the'))
print(myStr2.lower().count('the'))


#[8] capitalize()  
# converts the first character of a string to an uppercase letter and all other alphabets to lowercase.
#capitalizing the beginning of the sentences
print('-----------------[8 - capitalize() ]------------------')
myStr3 = 'the doctor was not present yesterday.. i was suppose to have my check up that day'

# split the string at '.' period
myList = myStr3.split('.')

# remove trailing white spaces
for num in range(0, len(myList)):
    myList[num] = myList[num].strip()

print(myList)

# use capitalize() with each member of the list
index_count = 0
while index_count < len(myList):
    myList[index_count] = myList[index_count].capitalize()
    index_count += 1

print(myList)

# join list members to make a new string
myStr3 = ''
for mem in range(0, len(myList)):
    myStr3 = myStr3 + myList[mem] + '. '
print(myStr3)

#[9] center(width, ' ') --> used to put padding character in the start and end of a string
# 1 split the string between \n
# 2 count the length of every string in the list created from split, put it in another list
# 3 find the max in the list that contain the length of every string from split()
# 4 put the max value as the width parameter of center()
print('-----------------[9 - center() ]------------------')
myStr4 = 'Hello I am Kaleb\n'\
         'I am from Calo\n'\
         'dog'
print(myStr4)
    # 1
myList = myStr4.split('\n')
print('')
print(f'myList {myList}')
print(' ')

index_count = 0
index_len = 0
List_len = [None] * len(myList)

    # 2
while index_count < len(myList):
    index_len = len(myList[index_count])
    List_len[index_count] = index_len
    index_count += 1
    #List
print(List_len)

    # 3
max_len = max(List_len)
print(f'{max_len} is max')

    # 4
print(' ')
print('centralized string. . . .')

index_count = 0

while index_count < len(myList):
    myList[index_count] = myList[index_count].center(max_len, ' ')
    index_count += 1

for mem in myList:
    print(mem)

#[10] endswith()/startswith() method returns True if a string ends with the specified suffix. 
print('-----------------[10 - endswith()/startswith() ]------------------')
message = 'Python is fun'

# check if the message ends with fun - returns a boolean
print(message.endswith('fun'))

#[11]  expandtabs() method returns a copy of string with all tab characters
# '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
print('-----------------[11 - expandtabs() ]------------------')
str = 'xyz\t12345\tabc'

print(str)

result = str.expandtabs(1) #default is 8 spaces if no argument

print(result)

#[12] encode() method returns an encoded version of the given string.
print('-----------------[12 - encode() ]------------------')

title = 'Python Programming'

# change encoding to utf-8
print(title.encode())

#[13] string.find(value, start, end)  method returns the index of first occurrence of the substring (if found). 
# If not found, it returns -1.
# note, its possible to use .find() to count occurence of a certain substring, using .count() is just better
print('-----------------[13 - find() ]------------------')
str3 = 'the dog is a big dog. I like that dog'
print(str3.find('dog'))


#[14] index() method returns the index of a substring inside the string (if found).
#  If the substring is not found, it raises an exception.
print('-----------------[14 - index() ]------------------')
text = 'the dog is a big dog. I like that dog'

# find the index of is
result = text.index('dog')
print(result)
# Output: 7

# python has also got the cctype-like functions like isalpha, isalnum, isdecimal, isdigit, isidentifier, 
# islower, isupper, isnumeric, isprintable, isspace, istitle, 

#[15] swapcase() method returns the string by converting all
#  the characters to their opposite letter case( uppercase to lowercase and vice versa).
print('-----------------[15 - swapcase() ]------------------')
name = "JoHn CeNa"

# converts lowercase to uppercase and vice versa
print(name.swapcase())

# Output: jOhN cEnA

#[16] strip(), lstrip(), rstrip() ---> removes both side, left or right
# strip() method returns a copy of the string by removing
#  both the leading and the trailing characters (based on the string argument passed).
print('-----------------[16 - strip() ]------------------')
message = '     Learn Python  '

# remove leading and trailing whitespaces
print(message.strip())

# Output: Message: Learn Python

#[17] translate() 
print('-----------------[17 - translate() ]------------------')
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

# maketrans()
# maketrans() method takes 3 parameters:

# x - If only one argument is supplied, it must be a dictionary.
# The dictionary should contain a 1-to-1 mapping from a single character string to its translation OR a Unicode number (97 for 'a') to its translation.
# y - If two arguments are passed, it must be two strings with equal length.
# Each character in the first string is a replacement to its corresponding index in the second string.
# z - If three arguments are passed, each character in the third argument is mapped to None.
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))


#[18] title() - returns a string with first letter of each word capitalized
print('-----------------[18 - title() ]------------------')
text = 'My favorite number is 25.'
print(text.title())

text = '234 k3l2 *43 fun'
print(text.title())

# zfill() - The width specifies the length of the returned string from zfill() with 0 digits filled to the left.
# used for filling zero in numbers


#rjust() and ljust() used to put padding

































