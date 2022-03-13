import util



def body():
    print('Nicely in a function')

    print('Toss 1 coins and get: {}'.format(util.toss_coin()))

    many = util.toss_coin_n(times=10)

    # let's compute how many of each
    # https://www.w3schools.com/python/ref_list_count.asp
    print('Toss 10 coins and get: {} heads, {} tails'.format(many.count('head'), many.count('tail')))
    # or
    heads = many.count('head')
    tails = len(many) - heads
    # or
    count = {'head': 0, 'tail': 0}
    for value in many:
        count[value] = count[value] + 1
    print(count)



#https://docs.python.org/3/library/__main__.html
#https://stackoverflow.com/questions/419163/what-does-if-name-main-do

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.  
    body()