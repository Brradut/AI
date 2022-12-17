import math

def argmax(x):
    maxi = 0
    max = x[0]
    for i in range(len(x)):
        if max < x[i]:
            max = x[i]
            maxi = i
    return maxi

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
