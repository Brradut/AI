import math
from mpl_toolkits import mplot3d
from sklearn.preprocessing import StandardScaler
import random
from lab6 import regressionError
import numpy
import matplotlib.pyplot as plt
from SGD import SGDBatch

def loadData(filename, ins, outs):

    f = open(filename)
    columns = f.readline()[:-1].split(',')
    print(columns)
    columnPosition = {}
    nrColumns = 0
    for c in columns:
        columnPosition[c] = nrColumns
        nrColumns = nrColumns + 1
     
    inputs = []
    outputs = []
    for r in f:
        row = r[:-1].split(",")
        try:
            [float(row[columnPosition[e]]) for e in ins]
            [float(row[columnPosition[e]]) for e in outs]
        except:
            continue
        inputs.append([float(row[columnPosition[e]]) for e in ins])
        outputs.append([float(row[columnPosition[e]]) for e in outs])
    
    return inputs, outputs
    

def prepareData(ins, outs):
    random.seed(5)
    dataSize = len(ins)
    indexes = [e for e in range(dataSize)]
    
    trainingSize = math.floor(dataSize * 0.8)
    testSize = dataSize - trainingSize
    
    trainingIndexes = random.sample(indexes, trainingSize)
    testIndexes = [e for e in indexes if e not in trainingIndexes]

    trainingInputs = [ins[e] for e in trainingIndexes]
    trainingOutputs = [outs[e] for e in trainingIndexes]
    testInputs = [ins[e] for e in testIndexes]
    testOutputs = [outs[e] for e in testIndexes]
    
    
    
    return [trainingInputs, trainingOutputs], [testInputs, testOutputs]



def main():
    d = loadData("2017.csv", ['Economy..GDP.per.Capita.','Freedom'], ['Happiness.Score'])#v2
   #d = loadData("data.csv", ['Economy..GDP.per.Capita.', 'Freedom'], ['Happiness.Score'])#v3
    data = prepareData(d[0], d[1])

    plt.plot(d[0], d[1], 'ro') 
    plt.xlabel('GDP capita')
    plt.ylabel('happiness')
    plt.title('GDP capita vs. happiness')
    plt.show()
    sgd = SGDBatch()
    sgd.fit(data[0][0], data[0][1])
    computedValues = [sgd.predict(e) for e in data[1][0]]
    print(regressionError(computedValues, realValues))

	
if __name__ == "__main__":
	main()
