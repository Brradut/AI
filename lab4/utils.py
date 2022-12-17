from random import randint

def generatePerm(n):
    v = []
    for i in range(0, n):
        v.append(i)

    p1 = randint(0, n - 1)
    p2 = randint(0, n - 1)

    v[p1], v[p2] = v[p2], v[p1]

    return v

def functieFitness(individ, matrix):
    d = 0.0
    lungime = len(individ)
    for i in range(lungime-1):
        d+=matrix[individ[i]][individ[i+1]]
    d+= matrix[individ[lungime-1]][individ[0]]
    return d

def getData(numeFisier):
    data = {}
    f = open(numeFisier, "r")
    n = int(f.readline())
    v=[[ ]*n]*n
    for i in range(0, n):
        v[i] = f.readline().split(",")
        for j in range(0, n):
            v[i][j]=int(v[i][j])
    source = int(f.readline())
    destination = int(f.readline())
    data['nrNoduri']=n
    data['matrix']=v
    return data
    
