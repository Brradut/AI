from utils import generateNewValue
from random import randint
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = [generateNewValue(problParam['nrNoduri']) for _ in range(problParam['nrNoduri'])]
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
        #two-way crossover
        r = randint(0, len(self.__repres) - 1)
        lbl1 = self.__repres[r]
        lbl2 = c.repres[r]
        newrepres1 = []
        newrepres2 = []
        for i in range(self.__problParam['nrNoduri']):
            if(self.__repres[i]==lbl1):
                newrepres1.append(lbl1)
            else:
                newrepres1.append(c.repres[i])
            if(c.repres[i] == lbl2):
                newrepres2.append(lbl2)
            else:
                newrepres2.append(self.__repres[i])
        
        offspring1 = Chromosome(self.__problParam)
        offspring1.repres = newrepres1
        offspring2 = Chromosome(self.__problParam)
        offspring2.repres = newrepres2
        return offspring1, offspring2
    
    def mutation(self):
        #changing a random node's label to a random label currently used
        source = randint(0, len(self.__repres) - 1)
        dest = randint(0, len(self.__repres)-1)
        self.__repres[dest] = self.__repres[source]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
