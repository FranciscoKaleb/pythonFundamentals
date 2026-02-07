print('-----------------[1 INPUT Basic]------------------')

print('What is your name?')
name = input()
print('Hello ' + name)


print('-----------------[2 Numbers]------------------')

print('Enter your daily wage:')
daily_wage = input()
print('Enter number of days worked this month:')
days_worked = input()

# we need convert the inputs to int and float for calculation. Python does not automatically convert str to int/float when doing arithmetic operations
monthly_wage = float(daily_wage)*int(days_worked)


print('Your monthly wage is: ' + str(monthly_wage)) # python does not automatically convert float to str when concatenating
# or you can use f-strings, which is more convenient
print(f'Your monthly wage is: {monthly_wage}') # f-strings automatically convert types when concatenating


