

# [3] while loop that keeps asking for input until input is out of range
keep_going = True

while keep_going:
    num = int(input('Enter a number between 1 and 10: '))
    
    if num < 1 or num > 10:
        print('Number out of range. Program end')
        keep_going = False
    else:
        print(f'You entered: {num}')