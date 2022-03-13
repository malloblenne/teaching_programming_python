# This program will check if the number from the user is the answer Answer to the Ultimate Question of Life, the Universe, and Everything
# or just an odd or even number

num = input('Write a number  here: ')

if num == 42:
    print('This is the Answer to the Ultimate Question of Life, the Universe, and Everything')
elif num % 2 == 0:
    print('This is an even numer')
else:
    print('This is an odd number')