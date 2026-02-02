
# [1]string formatting
print('-----------------[1]------------------')
sentence = "The {} bird is quite big"
sentence2 = "The {} pirate is {} tired"
sentence3 = "That {1} {0} cat is {2} white"
sentence4 = "The {a} old granny"

print(sentence.format('yellow')) # .format('string') inserts a string into another string inside the '{}'
print(sentence2.format('bad','super'))
print(sentence3.format('big','super','pure'))
print(sentence4.format(a = 'active'))
print(' ')

# [2]number, decimal formatting
print('-----------------[2]------------------')
result = 100/777
name = "Jose"
age = 20

print(result)
print("The result was {r}".format(r = result))
print(f'The result was {result}')
# manipulating decimal point
print("The result was {r:1.3f} inch".format(r = result))
print("The result was {r:9.3f} inch".format(r = result))
print(f'His name is {name}')
print(f'{name} is {age} years old')



