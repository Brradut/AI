from utils import getData
from utils import functieFitness
from Chromosome import Chromosome
from GA import GA
import os

def main():
    #load data
    filePath=os.path.join(os.getcwd(), "hard_01_tsp.txt")
    data = getData(filePath)
    
    #initial parameters
    GAparam = {'popSize':100, 'noGen':200}
    problParam = {'function':functieFitness, 'nrNoduri': data['nrNoduri'], 'matrix': data['matrix']}

    #solutions
    bestFitnesses = []
    averageFitnesses = []
    generations = []

    #initial generation
    ga = GA(GAparam, problParam)
    ga.initialisation()
    ga.evaluation()
    print(ga.bestChromosome())
    for g in range(GAparam['noGen']):
        c = ga.bestChromosome()
        bestFitnesses.append(c.fitness)
        averageFitnesses.append(sum([p.fitness for p in ga.population])/GAparam['popSize'])
        generations.append(g)

        print(ga.bestChromosome())
        #ga.oneGeneration()
        #ga.oneGenerationElitism()
        #ga.oneGenerationSteadyState()


main()