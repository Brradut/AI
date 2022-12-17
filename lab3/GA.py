from random import randint
from Chromosome import Chromosome
class GA:
    def __init__(self, param = None, problParam = None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []
        
    @property
    def population(self):
        return self.__population
    
    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
    
    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__problParam['context'])
            
    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best
        
    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if (self.__population[pos1].fitness > self.__population[pos2].fitness):
            return pos1
        else:
            return pos2 
        
    
    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']//2):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off1, off2 = p1.crossover(p2)
            off1.mutation()
            off2.mutation()
            newPop.append(off1)
            newPop.append(off2)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = []
        newPop.append(self.bestChromosome())
        for _ in range(self.__param['popSize']-1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off1, off2 = p1.crossover(p2)
            off1.mutation()
            newPop.append(off1)
        self.__population = newPop
        self.evaluation()
        
    def oneGenerationSteadyState(self):
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off1, off2 = p1.crossover(p2)
            off1.mutation()
            off2.mutation()
            off1.fitness = self.__problParam['function'](off1.repres,self.__problParam['context'])
            off2.fitness = self.__problParam['function'](off2.repres,self.__problParam['context'])
            worst = self.worstChromosome()
            if (off1.fitness < worst.fitness):
                worst = off1
            if(off2.fitness < worst.fitness):
                worst = off2
        self.evaluation()
