myString = "Hello World"

sub_string1 = myString[1]
sub_string2 = myString[-1] #get the last character 'd'
sub_string3 = myString[6:] #prints 'World' ----start at index 6 then print all
sub_string4 = myString[:6] #prints 'Hello ' ------print all, stop at index 6
sub_string5 = myString[1:5] #start at 1 end at 5, NOT include index 5
sub_string6 = myString[::2] # 2 is the interval of which index to copy
sub_string7 = myString[1:5:3] #start at index 1 and stop at 5, interval of 3
sub_string8 = myString[::-2] #copy the string in reverse interval

print(sub_string1)
print(sub_string2)
print(sub_string3)
print(sub_string4)
print(sub_string5)
print(sub_string6)
print(sub_string7)
print(sub_string8)
print("abcdefg"[::-1]) # direct without using variable