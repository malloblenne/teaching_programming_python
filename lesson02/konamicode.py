#https://en.wikipedia.org/wiki/Konami_Code
# Try to parse and find/detect the konami code given the user input, count how many times you find it




def solution(user_input):
    #add code here
    counter = 0

    for key in user_input:
        # add code here
        print('Sequence Found')

    return counter



if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    #
    konami_code = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'B', 'A']  
    
    sequence = konami_code
    print( 1 == solution(sequence))
    sequence = list(konami_code[0:5])*2 + list(konami_code) + list(konami_code[0:3]) 
    print( 1 == solution(sequence))
    sequence = list(sequence)*2
    print( 2 == solution(sequence))
    sequence = konami_code[0:8]
    print( 0 == solution(sequence))