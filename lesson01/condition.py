# Italians do it better. Fibonacci with his sequence proves the point.
# As everybody knows, Fibonacci sequence https://en.wikipedia.org/wiki/Fibonacci_number is the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# where a new number is made by the sum of the previous two numbers. It has important applications, even in Nature

# Write a program that print the first N Fibonacci numbers

total = input('How many Fibonacci numbers you would like to see on screen? ')

found = 1
n_minus1 = 0
n = 1

if total <= 0:
    print('NUmber too low')
    exit()

print('0')

while found < total:
    n_next = n + n_minus1 #just temporary. This is the main formula: n_(i+1) = n_i + n_(i-1)
    n_minus1 = n
    n = n_next
    print(n)
    found = found + 1
