


# to put delay in printing, use time.sleep(seconds)
import time
import random




myStr = 'hello'



# for x in range(0, len(myStr)+1, 1):
#    print(myStr[:x])



for x in range(len(myStr)-1, -1, -1):
   print(' ' * (len(myStr)-x-1), end = '')
   print(myStr[x::-1] + myStr[1:x+1])

for x in range(0, len(myStr)+1, 1):
   print(myStr[x:])










# for x in range(0, len(myStr)+1, 1):
#    for y in range(x):
#       print(myStr[y], end = '')
#    print()

# while(True):
#    myStr = random.choice(['Hello', 'World', 'Jupiter', 'cat', 'ambulance', 'sunlight', 'subic bay'])
#    for x in range(0, len(myStr), 1):
#       print(' ' * (len(myStr)-x-1), end = '')
#       for y in range(x, -1, -1):
#          print(myStr[y], end = '')
#          time.sleep(.0009)
#       for y in range(0, x + 1, 1):
#          print(myStr[y], end = '')
#          time.sleep(.0009)
#       print()

#    for x in range(len(myStr) - 1, -1, -1):
#       print(' ' * (len(myStr)-x-1), end = '')
#       for y in range(x, -1, -1):
#          print(myStr[y], end = '')
#          time.sleep(.0009)
#       for y in range(0, x + 1, 1):
#          print(myStr[y], end = '')
#          time.sleep(.0009)
#       print()





# 0
# 10
# 210
# 3210
# 43210

# 43210
# 3210
# 210
# 10
# 0

# 01234
# 0123
# 012
# 01
# 0













