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



def testP4():
    text = ["ana", "ana are", "ana ana are are ana are mere ana", "ana ana"]
    rez = [["ana"], ["ana", "are"], ["mere"], []]

    for i in range(len(text)):
        try:
            assert(P4(text[i]) == rez[i])
            print("Test #" + str(i) + " passed")
        except:
            print("Test #" + str(i) + " failed")




def P4(default=""):
    vect = []
    if len(default) == 0:
        vect = input("Introduceti textul:\n").split(" ")
    else:
        vect = default.split(" ")
    vect.sort()
    #sortam pentru a avea toate cuvintele care sunt la fel pe pozitii consecutive
    rez = []

    pre1 = ""
    pre2 = ""

    #luam o fereastra de 3 elemente, si comparam elementul din mijloc cu elementul de la stanga si dreapta
    #daca elementul din mijloc e diferit de ambele, atunci e unic in text
    if len(vect) > 1 and vect[0] != vect[1]:
        rez.append(vect[0])
    
    for v in vect:
        if pre1 == "" or pre2 == "":
            pre2 = pre1
            pre1 = v
        else:
            if pre1 != pre2 and pre1 != v:
               rez.append(pre1)
            pre2 = pre1
            pre1 = v
    if pre2 != pre1 and pre1 != "":
        rez.append(pre1)

    if len(default) == 0:
        print(rez)
    else:
        return rez


#Problema 5

def testP5():
    vect = ["1 2 3 4 2", "5 4 1 3 3 2", "1 2 1"]
    rez = [2, 3, 1]
    for i in range(len(vect)):
        try:
            assert(P5a(vect[i]) == rez[i])
            print("Test (a) #" + str(i) + " passed")
        except:
            print("Test (a) #" + str(i) + " failed")
        try:
            assert(P5b(vect[i]) == rez[i])
            print("Test (b) #" + str(i) + " passed")
        except:
            print("Test (b) #" + str(i) + " failed")

#a
def P5a(default=""):
    if len(default) == 0:
        vect = [int(x) for x in input("Introduceti elementele: ").split(" ")]
    else:
        vect = [int(x) for x in default.split(" ")]

    n = len(vect)
    v = []
    for i in range(0, n):
        v.append(0)
    for i in range(0, n):
        x = vect[i] -1
        #numerele incep de la 1, asa ca le shiftam sa inceapa de la 0
        v[x] = v[x] + 1
    rez = 0
    for i in range(0, n):
        if v[i] == 2:
            rez = i + 1
            #reversam shiftarea
            break
    if len(default) == 0:
        print(rez)
    else:
        return rez

#b
def P5b(default=""):
    vect = []
    if(len(default) == 0):
        vect = [int(x) for x in input("Introduceti elementele: ").split(" ")]
    else:
        vect = [int(x) for x in default.split(" ")]
    n = len(vect)
    rez = int(sum(vect) - ((n * (n-1))/2))
    if len(default) == 0:
        print(rez)
    else:
        return rez



#Problema 6

def testP6():
    vect = ["1 2 2", "2 2 2 1", "1 2 1 2 1 2 1"]
    rez = [2, 2, 1]

    for i in range(len(vect)):
        try:
            assert(P6(vect[i])==rez[i])
            print("Test #" + str(i) + " passed")
        except:
            print("Test #" + str(i) + " failed")



def P6(default=""):
    if len(default) == 0:
        v = [int(x) for x in input("Introduceti elementele: ").split(" ")]
    else:
        v = [int(x) for x in default.split(" ")]
    
    n = len(v)
    v.sort()
    #Dupa sortare, toate elementele egale for fi pe pozitii consecutive
    rez = v[n//2]
    if len(default) == 0:
        print("Elementul majoritar este: " + str(rez))
    else:
        return rez


#Problema 7


def testP7():
    v = ["1 3 7 4 1 5", "2 4 1 3 2", "7 6 5 3 1 4 7 3"]
    rez = [7, 3, 1]

    for i in range(len(v)):
        try:
            assert(P7(v[i]) == rez[i])
            print("Test #" + str(i) + " passed")
        except:
            print("Test #" + str(i) + " failed")




def P7(default=""):
    if len(default) == 0:
        vect = [ int(x) for x in input("Introduceti k, apoi elementele: ").split(" ")]
    else:
        vect = [int(x) for x in default.split(" ")]

    k = vect[0]
    v = vect[1:]
    n = len(v)
    v.sort()
    
    rez = v[n - k]


    if len(default) == 0:
        print("Al",k,"-lea cel mai mare element este:",rez)
    else:
        return v[n-k]


#Problema 8

def testP8():
    v = ["4", "1", "10"]
    rez = [["1", "10", "11", "100"], ["1"], ["1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010"]]
    for i in range(len(v)):
        try:
            assert(P8(v[i]) == rez[i])
            print("Test #" + str(i) + " passed")
        except:
            print("Test #" + str(i) + " failed")


def decToBin(x):
    s=""
    while x != 0:
        s = str(x%2) + s
        x = x//2
    return s

def P8(default=""):
    v = []
    if len(default) == 0:
        n = int(input("Introduceti numarul:"))
        for i in range(1, n+1):
          v.append(decToBin(i))
        print(v)
    else:
        n = int(default)
        for i in range(1, n+1):
            v.append(decToBin(i))
        return v



#Problema 10


def testP10():
    v = [[[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]], [[0, 0], [0, 1], [1, 1], [0, 1], [0, 0]], [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]]
    rez = [2, 3, 3]
    for i in range(len(v)):
        try:
            assert(P10a(v[i]) == rez[i])
            print("Test (a) #" + str(i) + " passed")
        except:
            print("Test (a) #" + str(i) + " failed")

        try:
            assert(P10b(v[i]) == rez[i])
            print("Test (b) #" + str(i) + " passed")
        except:
            print("Test (b) #" + str(i) + " failed") 



def P10a(default = []):
    v = []
    if len(default) == 0:
        n = int(input("Nr linii:"))
        m = int(input("Nr coloane:"))  
        v=[[]*m]*n
        for i in range(0, n):
            v[i] = input().split()
            for j in range(0, m):
                v[i][j]=int(v[i][j])
    else:
        v = default
        n = len(v)
        m = len(v[0])
    for i in range(0, m):
        for j in range (0, n):
            if v[j][i] == 1:    
                if len(default) == 0:
                    print("Linia",j+1,"are cele mai multe valori de 1")
                    return
                else:
                    return j + 1

def P10b(default = []):
    if len(default) == 0:
        n = int(input("Nr linii:"))
        m = int(input("Nr coloane:"))  
        v=[[]*m]*n
        for i in range(0, n):
            v[i] = input().split()
            for j in range(0, m):
                v[i][j]=int(v[i][j])
        mx = 0
        maxi = 0

        for i in range(0, n):
            s = sum(v[i])
            if mx < s:
                mx = s
                maxi = i
        print("Linia",maxi+1,"are cele mai multe valori de 1")
    else:
        mx = 0
        i = 1
        maxi = 0
        for line in default:
            s = sum(line)
            if mx < s:
                mx = s
                maxi = i
            i = i + 1
        return maxi
