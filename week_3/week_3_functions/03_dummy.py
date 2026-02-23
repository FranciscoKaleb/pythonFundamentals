

a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '



board = f'a |{a1}|{a2}|{a3}|\n'\
	f'b |{b1}|{b2}|{b3}|\n'\
	f'c |{c1}|{c2}|{c3}|\n'\
	 '   1 2 3'
	 
print(board)

num = 999

def print_num():
	global num
	num = num + 4
	print(num)
	
print_num()