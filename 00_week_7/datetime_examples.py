import datetime

def pause():
    """Pauses the script and waits for user input to continue."""
    if input('continue? [y/n] ').lower() != 'y':
        exit()

print('--------------------[1 Current date and time]----------------------------')
print('\n\n')

# 1. Current date and time

now = datetime.datetime.now() # yyyy-mm-dd hh:mm:ss.ms
print('Now:', now)
#this code will print datetime without milliseconds
print('Now (no ms):', now.replace(microsecond=0))
pause()

print('\n\n')
print('--------------------[2 Current date]----------------------------')
print('\n\n')

# 2. Current date
cur_date = datetime.date.today() # yyyy-mm-dd
print('Today:', cur_date)
pause()

print('\n\n')
print('--------------------[3 Create a date]----------------------------')
print('\n\n')

# 3. Create a date
print('Date:', datetime.date(2020, 5, 17))
pause()

print('\n\n')
print('--------------------[4 Create a time]----------------------------')
print('\n\n')

# 4. Create a time
print('Time:', datetime.time(12, 30))
pause()

print('\n\n')
print('--------------------[5 Format date]----------------------------')
print('\n\n')

# 5. Format date
print('Formatted:', now.strftime('%Y-%m-%d'))
pause()

print('\n\n')
print('--------------------[6 Parse date from string]----------------------------')
print('\n\n')

# 6. Parse date from string
parsed = datetime.datetime.strptime('2020-05-17', '%Y-%m-%d')
print('Parsed:', parsed)
pause()

print('\n\n')
print('--------------------[7 Timedelta]----------------------------')
print('\n\n')

# 7. Timedelta
delta = datetime.timedelta(days=5)
print('Timedelta:', delta)
pause()

print('\n\n')
print('--------------------[8 Add timedelta to date]----------------------------')
print('\n\n')

# 8. Add timedelta to date
future = now + delta
print('Future:', future)
pause()

print('\n\n')
print('--------------------[9 Difference between dates]----------------------------')
print('\n\n')

# 9. Difference between dates
start = datetime.date(2020, 5, 17)
end = datetime.date(2020, 5, 22)
print('Date diff:', end - start)
pause()

print('\n\n')
print('--------------------[10 Get weekday]----------------------------')
print('\n\n')

# 10. Get weekday
print('Weekday:', now.weekday())
pause()
