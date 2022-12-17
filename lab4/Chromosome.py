from utils import generatePerm
from random import randint
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = generatePerm(self.__problParam['nrNoduri'])
        self.__fitness = 0.0
    
    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
    
    def crossover(self, c):
        L = self.__problParam['nrNoduri']
        k = 0
        p1 = self.repres
        p2 = c.repres
        r1 = [-1] * L
        r2 = [-1] * L
        for i in range(L):
            r1[p1[i]]=i
            r2[p2[i]]=i

        v = [-1] * L
        while k != L:
            if v[k] == -1:
                if(k%2 == 1):
                    poz = k
                    v[poz] = p1[poz]
                    g = p2[poz]
                    poz = r1[g]
                    
                    while poz != k:
                        v[poz]=p1[poz]
                        g = p2[poz]
                        poz = r1[g]
                else:
                    poz = k
                    v[poz] = p2[poz]
                    g = p1[poz]
                    poz = r2[g]
                    
                    while poz != k:
                        v[poz]=p2[poz]
                        g = p1[poz]
                        poz = r2[g]
            k = k + 1
        offspring = Chromosome(self.__problParam)
        offspring.repres = v
        return offspring

    def mutation(self):
        p1 = randint(0, self.__problParam['nrNoduri'] - 1)
        p2 = randint(0, self.__problParam['nrNoduri'] - 1)
        if (p2 < p1):
            p1, p2 = p2, p1
        while (p1 < p2):
            self.__repres[p1], self.__repres[p2]=self.__repres[p2], self.__repres[p1]
            p1 += 1
            p2 -= 1

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
