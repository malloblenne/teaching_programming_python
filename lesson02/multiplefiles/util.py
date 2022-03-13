import random

def toss_coin():
    faces = ['head', 'tail']
    return faces[random.randint(0,1)]


def toss_coin_n(times):
    #return [toss_coin() for i in range(times)]
    
    results = []
    for i in range(times):
        results.append(toss_coin())
    return results