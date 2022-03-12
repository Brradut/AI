import networkx as nx
import numpy as np
import os

#reading network data from .gml file
def readNetwork(filename):
    filename = os.path.join(os.getcwd(), filename)
    G = nx.read_gml(filename)
    matrix = np.squeeze(np.asarray(nx.adjacency_matrix(G).todense()))
    params['matrix'] = matrix
    params['nrNoduri'] = len(matrix)
    degrees = []
    nrMuchii = 0
    for i in range(params['nrNoduri']):
        d = 0
        for j in range(params['nrNoduri']):
            if(matrix[i][j]==1):
                d+=1
            if(j > i):
                nrMuchii+=matrix[i][j]
        degrees.append(d)
    params['degrees'] = degrees
    params['nrMuchii'] = nrMuchii
    return params



def main():
    readNetwork("dolphins/dolphins.gml")


if __name__ == "__main__":
    main()



