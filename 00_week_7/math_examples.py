import math

def pause():
    """Pauses the script and waits for user input to continue."""
    if input('continue? [y/n] ').lower() != 'y':
        exit()

print('--------------------[1 Square root]----------------------------')
print('\n\n')

# 1. Square root
print('sqrt:', math.sqrt(16))
pause()

print('\n\n')
print('--------------------[2 Power]----------------------------')
print('\n\n')

# 2. Power
print('pow:', math.pow(2, 3)) # 2x2x2
pause()

print('\n\n')
print('--------------------[3 Floor]----------------------------')
print('\n\n')

# 3. Floor
print('floor:', math.floor(2.99))
pause()

print('\n\n')
print('--------------------[4 Ceil]----------------------------')
print('\n\n')

# 4. Ceil
print('ceil:', math.ceil(2.01))
pause()

print('\n\n')
print('--------------------[5 Factorial]----------------------------')
print('\n\n')

# 5. Factorial
print('factorial:', math.factorial(5))
pause()

print('\n\n')
print('--------------------[6 GCD]----------------------------')
print('\n\n')

# 6. GCD
print('gcd:', math.gcd(24, 18))
pause()

print('\n\n')
print('--------------------[7 Logarithm]----------------------------')
print('\n\n')

# 7. Logarithm
print('log:', math.log(100, 10))
pause()

print('\n\n')
print('--------------------[8 Trigonometry]----------------------------')
print('\n\n')

# 8. Trigonometry
print('sin:', math.sin(math.pi/2))
pause()

print('\n\n')
print('--------------------[9 Degrees to radians]----------------------------')
print('\n\n')

# 9. Degrees to radians
print('deg to rad:', math.radians(180))
pause()

print('\n\n')
print('--------------------[10 Radians to degrees]----------------------------')
print('\n\n')

# 10. Radians to degrees
print('rad to deg:', math.degrees(math.pi))
pause()
