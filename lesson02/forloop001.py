

basket1 = ['apple', 'kumbucha', 'banana', 'tofu']

for item in basket1:
    print(item)


basket1 = ['apple', 'kumbucha', 'banana', 'tofu']
basket2 = ['meat', 'fish', 'banana', 'tofu']
basket3 = ['apple', 'beer', 'banana', 'tofu']

mega_pokeball = [basket1, basket2, basket3]

for basket in mega_pokeball:
    print('this is now ', basket)
    for item in basket:
        print(item)


text = """I've seen things you people wouldn't believe.
Attack ships on fire off the shoulder of Orion.
I watched c-beams glitter in the dark near the Tannhuser Gate.
All those moments will be lost in time, like tears in rain.
Time to die."""

print(text)

print('\n\nsome spaces\n\n\n')

n_line = 0
for line in text.splitlines():
    print(str(n_line) + ' ' + line)
    n_line += 1

print('\n\nsome spaces\n\n\n')

# Yoda style
for line in text.splitlines():
    words = line.split(' ')
    words.reverse()
    #make one string with spaces
    new_line = str(' ').join(words)  # ' '.join(words) 
    print(new_line)