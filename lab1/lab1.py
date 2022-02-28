import math

#Daca nu primim parametru, presupun ca inputul si outputul se iau de la consola
#Daca primim parametru, returnam rezultatul


 #Problema 1

def P1(default=""):
    if len(default) == 0:
        cuvinte = input("Introduceti cuvintele\n").split(" ")
    else:
        cuvinte = default.split(" ")
    max = ""
    for cuvant in cuvinte:
        if max.upper() < cuvant.upper():    
            max = cuvant
    if(len(default) == 0):
        print(max)
    else:
        return(max)

def testP1():
    fraze = ["Zebre doi trei", "Una bucata Zebra", "Am sa merg si am sa merg iar"]
    raspunsuri = ["Zebre", "Zebra", "si"]
    for i in range(len(fraze)):
        try:
            assert(P1(fraze[i]) == raspunsuri[i])
            print("Test #" + str(i) + " passed")
        except:
            print("Test #" + str(i) + " failed")




#Problema 2


def radical(x, p=0.001):
    st = 0
    dr = x
    while st <= dr:
        mij = (st + dr)/2
        if mij * mij + p >= x and mij * mij - p <= x:
            return mij
        if mij * mij < x:
            st = mij
        else:
            dr = mij



def P2(default=""):
    if len(default) == 0:
        x1,y1=input("Introduceti primul punct:\n").split(" ")
        x2,y2=input("Introduceti al 2-lea punct:\n").split(" ")
    else:
        x1, y1, x2, y2 = default.split(" ")

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    rez = radical((x1-x2) * (x1 - x2) + (y1 - y2) * (y1-y2))
    if len(default)==0:
        print("Distanta este: ", "{:.2f}".format(round(rez, 2)))
    else:
        return round(rez, 2)


def testP2():
    puncte = ["6 8 4 1", "8 3 10 5", "6 5 7 4"]
    rez = [7.28, 2.83, 1.41]

    for i in range(len(puncte)):
        try:
            assert(round(P2(puncte[i]), 2) == rez[i])
            print("Test #" + str(i) + " passed")
        except:
            print("Test #" + str(i) + " failed")

#Problema 3

def P3():
    n = int(input("Introduceti lungimea vectorilor: "))
    v1 = []
    v2 = []
    v1 =[int(x) for x in input("Elementele primului vector: ").split(" ")]
    v2 =[int(x) for x in input( "Elementele celui de-al doilea vector: ").split(" ")]
    s =  sum([v1[i] * v2[i] for i in range(0, n)]) 
    print("Produsul scalar este: ",s)

#Problema 4

def P4():
    vect = input("Introduceti textul:\n").split(" ")
    vect.sort()
    pre1 = ""
    pre2 = ""
    for v in vect:
        if pre1 == "" or pre2 == "":
            pre2 = pre1
            pre1 = v
        else:
            if pre1 != pre2 and pre1 != v:
                print(pre1)
            pre2 = pre1
            pre1 = v
    if pre2 != pre1 and pre1 != "":
        print(pre1)


#Problema 5
def P5():
    n = int(input("Introduceti numarul de elemente:"))
    v = []
    for i in range(0, n):
        v.append(0)
    for i in range(0, n):
        x = int(input("Elementul $i:"))
        v[x] = v[x] + 1
    for x in v:
        if x == 2:
            print("Rezutatul este: ",x)
            break

#Problema 6

def P6():
    n = int(input("Nr elemente:"))
    v = []
    for i in range(0, n):
        v.append(int(input()))
    v.sort()
    for i in range(0, n//2):
        if(v[i] == v[i+ n//2]):
            print("Elementul majoritar este:",v[i])
            break

#Problema 7

def P7():
    n = int(input("Nr elemente:"))
    k = int(input("Introduceti k:"))
    print("Elementele:")
    v = []
    for i in range(0, n):
        v.append(int(input()))
    v.sort()
    print("Al",k,"-lea cel mai mare element este:",v[n-k])

#Problema 8

def decToBin(x):
    s=""
    while x != 0:
        s = str(x%2) + s
        x = x//2
    return s

def P8():
    n = int(input("Introduceti numarul:"))
    for i in range(1, n+1):
        print(decToBin(i))


#Problema 10

def P10a():
    n = int(input("Nr linii:"))
    m = int(input("Nr coloane:"))  
    v=[[]*m]*n
    for i in range(0, n):
        v[i] = input().split()
        for j in range(0, m):
            v[i][j]=int(v[i][j])
    for i in range(0, m):
       for j in range (0, n):
           if v[j][i] == 1:
               print("Linia",j+1,"are cele mai multe valori de 1")
               return

def P10b():
    n = int(input("Nr linii:"))
    m = int(input("Nr coloane:"))  
    max = 0
    maxi = 0
    for i in range(0, n):
        sum = 0
        x = input().split()
        for j in range(0, m):
            sum = sum + int(x[j])
        if max < sum:
            max = sum
            maxi = i
    print("Linia",maxi+1,"are cele mai multe valori de 1")       
