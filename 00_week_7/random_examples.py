import random

def pause():
    """Pauses the script and waits for user input to continue."""
    if input('continue? [y/n] ').lower() != 'y':
        exit()

print('--------------------[1 Random integer]----------------------------')
print('\n\n')

# 1. Random integer
print('randint:', random.randint(1, 10))
pause()

print('\n\n')
print('--------------------[2 Random float]----------------------------')
print('\n\n')

# 2. Random float
print('random:', random.random())
pause()

print('\n\n')
print('--------------------[3 Random choice]----------------------------')
print('\n\n')

# 3. Random choice
print('choice:', random.choice(['apple', 'banana', 'cherry']))
pause()

print('\n\n')
print('--------------------[4 Random sample]----------------------------')
print('\n\n')

# 4. Random sample
for i in range(100):
    print('sample:', random.sample([1, 2, 3, 4, 5], 3))
pause()

print('\n\n')
print('--------------------[5 Shuffle list]----------------------------')
print('\n\n')

# 5. Shuffle list
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print('shuffled:', lst)
pause()

print('\n\n')
print('--------------------[6 Seed random]----------------------------')
print('\n\n')

# 6. Seed random
# random.seed() controls how random numbers are generated.

# Python doesn’t generate true randomness—it uses a formula (algorithm).
# The seed is the starting point of that formula.

for x in range(20):
    print(random.randint(1, 10), end=' ') # no seed - this will generate a different sequence of random numbers every time we run the script

print('\n\n')
random.seed(1)
for x in range(20):
    print(random.randint(1, 10), end=' ') # this will generate the same sequence of random numbers every time we run the script because we set the seed to 1
# 3 10 2 5 2 8 8 8 7 4 2 8 1 7 7 10 1 8 5 4
pause()

print('\n\n')
print('--------------------[7 Uniform float]----------------------------')
print('\n\n')

# 7. Uniform float - It generates a random float (decimal number) between two values.
print('uniform:', random.uniform(1, 10))
pause()

print('\n\n')
print('--------------------[8 Random choices with weights]----------------------------')
print('\n\n')

# 8. Random choices with weights
print('choices:', random.choices(['a', 'b', 'c'], weights=[5, 1, 1], k=5)) # this will generate more 'a' than 'b' and 'c' because of the weights
pause()

print('\n\n')
print('--------------------[9 Random range]----------------------------')
print('\n\n')

# 9. Random range
print('randrange:', random.randrange(0, 100, 5)) # this will generate a random number from 0 to 100 that is divisible by 5
pause()

print('\n\n')
print('--------------------[10 Random boolean]----------------------------')
print('\n\n')

# 10. Random boolean
print('random boolean:', random.choice([True, False])) # this will generate a random boolean value
pause()
