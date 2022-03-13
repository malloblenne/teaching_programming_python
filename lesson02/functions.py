
import math

# return is the output the variables in paranthesis are the parameters, often just input
def my_sum(elem1, elem2):
    return elem1 + elem2


# how to use it

print( my_sum(1, 3))

a = 1
b = 41
the_sum = my_sum(a,b)
# or also
the_sum = my_sum(elem1=a, elem2=b)

#arguments are evaluated before passed to function

the_great_sum = my_sum(my_sum(1,2),my_sum(my_sum(b, -10), 0))
print(the_great_sum)

# functions can have their own local variables

def upper_lower(input_str):
    upper = input_str.upper()
    return upper + input_str.lower()

up_down = upper_lower('DigiEvolution')
print(up_down)


# functions can be recursive (but better not to)

#interesting to look at the call stack
def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))

def factorial_for(n):
    res = 1
    for i in range(1,n+1):
        res*= i
    return res

print(factorial_recursive(5) == factorial_for(5))

print(math.prod(range(1,5+1)))

# lambda function, advanced, no need to learn :P
factorial_oneliner = lambda x : math.prod(range(1,x+1))

print(factorial_oneliner(5))


######### what happens with mutable/immutable data types

def fun_immutable(mydata):
    mydata = 5
    print(mydata)

mydata=6
fun_immutable(mydata)
print(mydata)


def fun_mutable(mylist):
    mylist.append('kombucha')
    print(mylist)

myotherlist = ['mariobros', 'guardian legend']
print(fun_mutable(myotherlist))



### variables and global variables


alpha = 1

def my_local_var():
    alpha = 3
    print(alpha)
    return 72

hello = my_local_var()
print(alpha)


def my_global_var():
    global alpha
    alpha = 32
    return (2, 3, 4)


print(alpha)
my_global_var()
print(alpha)

