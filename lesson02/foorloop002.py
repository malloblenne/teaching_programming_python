import random

interval = range(0,10)



table = []
for r in range(5):
    row = []
    for c in range(6):
        row.append(random.randint(1,20))
    table.append(row)

print(table)


# find the first value from top left to bottom right with value 19
found = False
for r in range(len(table)):
    for c in range(len(table[0])):
        print('Value in consideration is ', table[r][c])
        if table[r][c] == 19 and not found:
            print('Element 19 is in (' + str(r) + ', ' + str(c) + ')')
            found = True


# find the first value from top left to bottom right with value 19
for r in range(len(table)):
    already_found = False
    for c in range(len(table[0])):
        print('Value in consideration is ', table[r][c])
        if table[r][c] == 19:
            print('Element 19 is in (' + str(r) + ', ' + str(c) + ')')
            already_found = True
            break
    if already_found:
        break




# enumerate
#https://en.wikipedia.org/wiki/Seven_Dwarfs#Disney_Dwarfs
dwarfs = ['Grumpy', 'Dopey', 'Doc', 'Happy', 'Bashful', 'Sneezy', 'Sleepy', 'Dopey'] 
for index, item in enumerate(dwarfs):
    #print(item + ' is the dwarf number ' + str(index))
    print('{} is the dwarf number {}'.format(item, index))


#  with function

def find_elem_table(table, elem):
    for r in range(len(table)):
        for c in range(len(table[0])):
            if table[r][c] == elem:
                return [r,c]
    return None

row_col = find_elem_table(table, 19)
if row_col:
    print('Element 19 is in (' + str(row_col[0]) + ', ' + str(row_col[1]) + ')')


# function just find if it is there
def find_ifthere_elem_table(table, elem):
    for r in range(len(table)):
        if elem in table[r]:
            return True
    return False

print('Found it!' if find_ifthere_elem_table(table, 19) else 'Not found :(')

