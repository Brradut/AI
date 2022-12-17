import networkx as nx
import numpy as np
import os
from random import randint
def generateNewValue(max):
    #generates a new label <= max
    return randint(1, max)

def readNetwork(filename):
    G = nx.read_gml(filename, label='id')
    params = {}
    matrix = np.squeeze(np.asarray(nx.adjacency_matrix(G).todense()))
    params['matrix']=matrix
    params['nrNoduri']=len(matrix)
    degrees=[]
    nrMuchii=0.0
    muchii=[]
    for i in range(params['nrNoduri']):
        d = 0
        for j in range(params['nrNoduri']):
            if(matrix[i][j] == 1):
                muchii.append([i, j])
                d+=1
            if(j >i):
                nrMuchii+=matrix[i][j]
        degrees.append(d)
    params['degrees']=degrees
    params['nrMuchii']=nrMuchii
    params['muchii']=muchii
    return params


