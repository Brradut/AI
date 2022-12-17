from utils import readNetwork
from Chromosome import Chromosome
from GA import GA
import os
def modularity(communities, param):
    nrNoduri = param['nrNoduri']
    matrix = param['matrix']
    degrees = param['degrees']
    nrMuchii = param['nrMuchii']  
    M = 2 * nrMuchii
    Q = 0.0
    for i in range(0, nrNoduri):
        for j in range(0, nrNoduri):
            if (communities[i] == communities[j]):
               Q += (matrix[i][j] - (degrees[i] * degrees[j]) / M)
    return  Q * 1 / M

def modularityDensity(communities, param):
    nrNoduri = param['nrNoduri']
    matrix = param['matrix']
    degrees = param['degrees']
    nrMuchii = int(param['nrMuchii'])  
    muchii = param['muchii']
    nrComunitati = len({e for e in communities})
    D=0.0
    v = {}
    k = {}
    for i in range(nrNoduri):
        k[communities[i]]=0.0
        v[communities[i]]=0.0
    for i in range(nrNoduri):    
        k[communities[i]]+=1
    for m in muchii:
        if communities[m[0]] == communities[m[1]]:
            v[communities[m[0]]]+=1.0
        else:
            v[communities[m[0]]]-=1.0
    
    for i in v:
        D+=v[i]/k[i]
    return  D

def main():
    #load data
    filePath=os.path.join(os.getcwd(), 'real', 'football', 'football.gml')
    network = readNetwork(filePath)
    
    #initial parameters
    GAparam = {'popSize':100, 'noGen':100}
    problParam = {'function':modularity, 'nrNoduri': network['nrNoduri'], 'context':network}

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

        print(ga.bestChromosome().fitness)#, "Nr comunitati:",len({e for e in ga.bestChromosome().repres}))
        #ga.oneGeneration()
        #ga.oneGenerationElitism()
        ga.oneGenerationSteadyState()
    nrComunitati=len({e for e in ga.bestChromosome().repres})

    #for j in range(nrComunitati):
     #   for i in range(len(ga.bestChromosome().repres)):
            #print("Nod in comunitate:",j, i)
    
   
    print(ga.bestChromosome(), "Nr comunitati:",len({e for e in ga.bestChromosome().repres}))
    
    
if __name__ == "__main__":
    main()
