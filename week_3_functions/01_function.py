#[1] creating a function
print('-----------------[1]------------------')
def name_of_function(): # snake case is the common practice in python
    print('hello world')

    
#[2] calling a function
print('-----------------[2]------------------')
name_of_function()

#[3] parameters
print('-----------------[3]------------------')
def greet(name):
    print(f'hello {name}')
name = 'Jose'
print(f'name = {name}')
greet(name)

#[4] returning values
print('-----------------[4]------------------')
def greet_2(name):
    return f'hello {name}'

str = greet_2(name)
print(str)

#[5] function that takes two parameters and adds them
print('-----------------[5]------------------')
def add(num1, num2):
    return num1 + num2

print(add(2, 6))

#[6] default values - trigger if no argument are passed
print('-----------------[6]------------------')
def add(num1 = 0, num2 = 0):
    return num1+num2

print(add()) # prints 0

#[7] Python Function With Arbitrary Arguments
# factorial example 4x3x2x1
print('-----------------[7]------------------')
    # example 1
def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num
    return result

print(find_sum(1,77,89,56))
    # example 2
def concat_strings(*strings):
    result = ''

    for sub_s in strings:
        result = result + sub_s + ' '
    
    return result

print(concat_strings('Francisco', 'Kaleb', 'Marquez'))

#[8] Recursion
print('-----------------[8]------------------')
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    # lets say its a factorial of 4, the result is like
    #  1st 4 * 
    #  2nd 3 *
    #  3rd 2 *
    #  4th 1

num = 3
print("The factorial of", num, "is", factorial(num))

# [9]Python lambda

print('-----------------[9]------------------')
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Delilah')

# Output: Hey there, Delilah

#[10] function with logic
print('-----------------[10]------------------')
myList = [2,2,2,29,4,8]

def check_if_all_even(num_list):
    result = True
    for num in num_list:
        if num%2 != 0:
            result = False
    return result

is_even = check_if_all_even(myList)

print(f'all number in the list is even - {is_even}')

#[11] filter odd numbers in a list 
print('-----------------[11]------------------')
myList = [1,2,3,4,5,6,7,8,9,10]

def filter_odd(num_list):
    new_list = []
    for num in num_list:
        if num%2 == 0:
            new_list.append(num)
        else:
            pass
    return new_list

my_even_list = filter_odd(myList)

print(f'original list - {myList}')
print(f'new list - {my_even_list}')

#[12] tuple unpacking to select best employee based on work hours
print('-----------------[12]------------------')
employee_work_hours = [('Abby', 80), ('Jose', 100), ('Karen', 110), ('Susan', 102)]

def employee_check(list):
    current_max = 0
    employee_of_month = ''

    for employee, hours in list:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)

best_employee = employee_check(employee_work_hours)

print(best_employee)

#[13] interaction between functions
print('-----------------[13]------------------')
# guessing the index of a shuffled list game

# 1 create an initial list
myList = [' ', 'O', ' ']

# 2 import shuffle
from random import shuffle

# 3 create a function that accepts a list, shuffle the list, and return the shuffled list
def shuffle_list(list):
    shuffle(list)
    return list

# 4 create a function that requests an number input from 0 - 2
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        print('number must be either 0, 1 or 2')
        print(f'enter number: ')
        guess = input()
    return guess

# 5 create a function that accepts the mixed list, and the index guess. It will process if the guess is right
def check_guess(mixedup_list, guess):
    guess = int(guess)
    if mixedup_list[guess] == 'O':
        print('your guess is right')
    else:
        print('wrong guess')

# shuffle test
mixedup_list = shuffle_list(myList)

# user guess loop, will repeat if input is incorrect
guess = player_guess()

# check guess
check_guess(mixedup_list, guess)
print(mixedup_list)




