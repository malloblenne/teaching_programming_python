#https://docs.python.org/3/library/stdtypes.html

basket = ['apple', 'kumbucha', 'banana', 'tofu']
print(basket[1])
print(basket[0])

print(basket)

basket.reverse()
print(basket)
basket.append('soya sauce')
print(basket)
print(basket[0:3])
basket = basket[0:3]
basket.remove('tofu')
print(basket)

basket[1] = 'pomelo'
print(basket)

basket1 = ['apple', 'kumbucha', 'banana', 'tofu']
basket2 = ['meat', 'fish', 'banana', 'tofu']
basket3 = ['apple', 'beer', 'banana', 'tofu']

mega_pokeball = [basket1, basket2, basket3, 42]

print(mega_pokeball)
print('Length of list is ' + str(len(mega_pokeball)))
print(mega_pokeball[0][2])


mybasket_copy = basket1
print(mybasket_copy)
basket1.append('cilantro')
print(mybasket_copy)
mybasket_copy = list(basket1)
basket1.append('tomato')
print(mybasket_copy)
print(basket1)


# https://docs.python.org/3/tutorial/datastructures.html