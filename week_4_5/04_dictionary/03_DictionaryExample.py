


#[1] word counting
myStr = "From From fairest creatures we desire increase,\n"\
        "That thereby beauty's rose might never die,\n"\
        "But as the riper should by time decease,\n"\
        "His tender heir might bear his memory:\n"\
        "But thou contracted to thine own bright eyes,\n"\
        "Feed'st thy light's flame with self-substantial fuel,\n"\
        "Making a famine where abundance lies,\n"\
        "Thy self thy foe, to thy sweet self too cruel:\n"\
        "Thou that art now the world's fresh ornament,\n"\
        "And only herald to the gaudy spring,\n"\
        "Within thine own bud buriest thy content,\n"\
        "And tender churl mak'st waste in niggarding:\n"\
        "Pity the world, or else this glutton be,\n"\
        "To eat the world's due, by the grave and to thee.\n       "

# replace symbols with space
def replaceSymbol(myStr):
    myStr = myStr.replace('\n', ' ')
    myStr = myStr.replace('\r', ' ')
    myStr = myStr.replace('\t', ' ')
    myStr = myStr.replace(',', ' ')
    myStr = myStr.replace(':', ' ')
    myStr = myStr.replace(';', ' ')
    myStr = myStr.replace('.', ' ')
    myStr = myStr.replace('?', ' ')
    myStr = myStr.replace('!', ' ')
    return myStr

def strToList(myStr):
    new_list = myStr.split(' ')
    return new_list

myStr = replaceSymbol(myStr)
new_list = strToList(myStr)
new_dictionary = {}

# count the list using dictionary

# loop through the list and set initial count per key to zero
for mem in new_list:
    new_dictionary.setdefault(mem, 0)

# loop through the same list again and increment key count each time string appear
for mem in new_list:
    new_dictionary[mem] = new_dictionary[mem] + 1

# SORT 1: Alphabetically. sort it alphabetically using key
alphabetically_sorted_list = sorted(new_dictionary)

print('--------sort alphabetically--------')
for mem in alphabetically_sorted_list:
    print(f'{mem} : {new_dictionary[mem]}')






# SORT 2: based on value. sort it by word count using value
# turn the dictionary in list of tuple pair so we can apply sorted() function into it
list_of_tuple_pair = []
for mem in new_dictionary:
    # appending a tuple pair in a list
    list_of_tuple_pair.append((mem, new_dictionary[mem]))

print('--------sort based on VALUE--------')

def take_second(elem):
    return elem[1]

sorted_list_of_tuple_pair = sorted(list_of_tuple_pair, key = take_second, reverse = True)

for (key,value) in sorted_list_of_tuple_pair:
    print(f'{key} : {value} ')

