import math
from mpl_toolkits import mplot3d
import random
from linearRegressor import ToolLinearRegressor
from linearRegressor import CustomLinearRegressor
from lab6 import regressionError
import numpy
import matplotlib.pyplot as plt

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

def plotHist(x, name):
    n, bins, patches = plt.hist(x, 10)
    plt.title('Histogram of ' + name)
    plt.show()
    



def main():
    #d = loadData("v1_world-happiness-report-2017.csv", ['Economy..GDP.per.Capita.'], ['Happiness.Score'])#v1
    d = loadData("v2_world-happiness-report-2017.csv", ['Economy..GDP.per.Capita.','Freedom'], ['Happiness.Score'])#v2
    #d = loadData("data.csv", ['Economy..GDP.per.Capita.', 'Freedom'], ['Happiness.Score'])#v3
    data = prepareData(d[0], d[1])
    regressor = ToolLinearRegressor()
    #regressor = CustomLinearRegressor()
    regressor.fit(data[0][0], data[0][1])
    realValues = data[1][1]
    computedValues = [regressor.predict(e) for e in data[1][0]]
    # for r, c in zip(computedValues, realValues):
    #    print(r, c)
    print(regressionError(computedValues, realValues))
    
    #print(data[0][0])
    #capita = []
    #freedom = []
    #print(data[0][0])
    #for elem in data[0][0]:
    #    capita.append(elem[0])
    #    freedom.append(elem[0])
    #plotHist(capita, 'GDP')
    #plotHist(freedom, 'freedom')
    #plotHist(data[0][1], 'happiness')
    
    
    trainGDP=[]
    trainFreedom=[]
    for elem in data[0][0]:
        trainGDP.append(elem[0])
        trainFreedom.append(elem[1])
    valGDP = []
    valFreedom = []
    for elem in data[1][0]:
        valGDP.append(elem[0])
        valFreedom.append(elem[1])

    trainOutputs = data[0][1]
    validationOutputs = data[1][1]


    w0, w1, w2 = regressor._ToolLinearRegressor__weights[0][0], regressor._ToolLinearRegressor__weights[1][0], regressor._ToolLinearRegressor__weights[2][0]
    #w0, w1, w2 = regressor._CustomLinearRegressor__weights[0], regressor._CustomLinearRegressor__weights[1], regressor._CustomLinearRegressor__weights[2]

    print(w0, w1, w2)
    noOfPoints = 1000
    xref = []
    xxref = []
    yref = []
    valx = min(trainGDP)
    valy = min(trainFreedom)
    stepx = (max(trainGDP) - min(trainGDP)) / noOfPoints
    stepy = (max(trainFreedom) - min(trainFreedom)) / noOfPoints
    for i in range(1, noOfPoints):
        xref.append(valx)
        xxref.append(valy)
        valx += stepx
        valy += stepy
    for x1,x2 in zip(xref,xxref):
        yref.append(w0+w1*x1+w2*x2)

    fig = plt.figure(figsize=(6,6))
    ax = plt.axes(projection='3d')
    ax.scatter(trainGDP,trainFreedom, trainOutputs, 'ro', label = 'train data') 
    ax.scatter(xref,xxref, yref, 'b-', label = 'learnt model') 
    plt.title('train data and the learnt model')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
