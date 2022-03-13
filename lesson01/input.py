# This program gets and input from the user and print it

s = input('Write a number of a string using \' or \"  here: ')
print(s)
print(type(s))

# This only works if we can cast it to a number
print('The following works only with numbers')
print(int(s))
print(type(int(s)))