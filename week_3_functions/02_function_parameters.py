


print('--- 01 Function Parameters ---')
def greet(name):
    print(f'hello {name}')
    
name = 'Jose'
greet(name)
print()

print('--- 02 Function Parameters ---')


def add(num1, num2):
    return num1 + num2

print(add(2, 6))
print()

print('--- 03 basic input ---')

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
sum = add(num1, num2)
print(f'{num1} + {num2} = {sum}')