from logisticRegression import LogisticRegressor
from logisticRegressionMulti import LogisticRegressorMulti
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
import random
import math
from utils import sigmoid
from lab6 import classificationError, lossClassificationMultiClass
import sklearn.linear_model
from utils import argmax

def prepareData1(ins, outs, ratio = 0.8):
    scaler = StandardScaler()

    scaler.fit(ins)
    ins = scaler.transform(ins)
    
    random.seed(5)
    dataSize = len(ins)
    indexes = [e for e in range(dataSize)]
    
    trainingSize = math.floor(dataSize * ratio)
    testSize = dataSize - trainingSize
    
    trainingIndexes = random.sample(indexes, trainingSize)
    testIndexes = [e for e in indexes if e not in trainingIndexes]

    insT = [ins[e] for e in trainingIndexes]
    outsT = [outs[e] for e in trainingIndexes]
    insV = [ins[e] for e in testIndexes]
    outsV = [outs[e] for e in testIndexes]

    return insT, outsT, insV, outsV


def prepareData2(ins, outs , ratio = 0.9):
    labels = []
    for x in outs:
        if x not in labels:
            labels.append(x)
    y = []
    for x in outs:
        yy = [0] * len(labels)
        for i in range(len(labels)):
            if labels[i] == x:
                yy[i] = 1
        y.append(yy)

    outs = y

    scaler = StandardScaler()

    scaler.fit(ins)
    ins = scaler.transform(ins)
    
    random.seed(5)
    dataSize = len(ins)
    indexes = [e for e in range(dataSize)]
    
    trainingSize = math.floor(dataSize * ratio)
    testSize = dataSize - trainingSize
    
    trainingIndexes = random.sample(indexes, trainingSize)
    testIndexes = [e for e in indexes if e not in trainingIndexes]

    insT = [ins[e] for e in trainingIndexes]
    outsT = [outs[e] for e in trainingIndexes]
    insV = [ins[e] for e in testIndexes]
    outsV = [outs[e] for e in testIndexes]

    return insT, outsT, insV, outsV



#Data loaded from a csv file. We use the 2nd, 3rd and 4th rows (type of cancer, radius of nucleous, texture)
def loadData1():
    filename = 'wdbc.data'
    f = open(filename, 'r')
    
    ins = []
    outs = []

    for line in f.readlines():
        cols = line[:-1].split(",")
        ins.append([float(cols[2]), float(cols[3])])
        if cols[1] == 'M':
            outs.append(1)
        else:
            outs.append(0)
    return ins, outs

def loadData2():
    filename = 'iris.data'
    f = open(filename, 'r')
    
    ins = []
    outs = []

    for line in f.readlines():
        cols = line[:-1].split(",")
        ins.append([float(cols[0]), float(cols[1]), float(cols[2]), float(cols[3])])
        outs.append(cols[4])
    return ins, outs


def p1():
    prag = 0.5
    ins, outs = loadData1()
    insT, outsT, insV, outsV = prepareData1(ins, outs)
    
    xT = []
    yT = []
    zT = []

    xV = []
    yV = []
    zV = []
    
    for i in range(len(insT)):
        xT.append(insT[i][0])
        yT.append(insT[i][1])
        zT.append(outsT[i]) 
    
    for i in range(len(insV)):
        xV.append(insV[i][0])
        yV.append(insV[i][1])
        zV.append(outsV[i]) 
    #custom regressor
    regressor = LogisticRegressor()
    regressor.fit(insT, outsT)
    
    w0, w1, w2 = regressor._LogisticRegressor__weights[0],regressor._LogisticRegressor__weights[1],regressor._LogisticRegressor__weights[2]
    xW = np.linspace(min(np.array(insT)[:,0]),max(np.array(insT)[:,0]), 1000)
    yW = np.linspace(min(np.array(insT)[:,1]), max(np.array(insT)[:,1]), 1000)
    zW = regressor.predict([[x, y] for x, y in zip(xW, yW)])
    
    ycomputed = []
    for i in regressor.predict(insV):
        if i >= prag:
            ycomputed.append(1)
        else:
            ycomputed.append(0)

    acc, [preciziePoz, precizieNeg], [rapelPoz, rapelNeg] = classificationError(ycomputed, outsV, 1)
    print(f'custom logistic regressor:')
    print(f'model: {w0} + x1 * {w1} + x2 * {w2}')
    print(f'acc:{acc}, precizie:{preciziePoz}, rapel: {rapelPoz}')
    #tool regressor
    regressor_tool = sklearn.linear_model.LogisticRegression()
    regressor_tool.fit(insT, outsT)
    ww0, ww1, ww2 = regressor_tool.intercept_[0], regressor_tool.coef_[0][0], regressor_tool.coef_[0][1]
    zzW = regressor_tool.predict([[x,y] for x, y in zip(xW, yW)])
    
    ycomputed = regressor_tool.predict(insV)

    acc, [preciziePoz, precizieNeg], [rapelPoz, rapelNeg] = classificationError(ycomputed, outsV, 1)
    print(f'\nsklearn logistic regressor:')
    print(f'model: {ww0} + x1 * {ww1} + x2 * {ww2}')
    print(f'acc:{acc}, precizie:{preciziePoz}, rapel: {rapelPoz}')
   

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(xT, yT, zT, 'r*', label = 'training data')
    ax.scatter(xV, yV, zV, 'b*', label = 'test data')
    ax.scatter(xW, yW, zW, 'g-', label = 'model')
    ax.scatter(xW, yW, zzW, 'y-', label = 'model2')
    ax.set_xlabel('Radius')
    ax.set_ylabel('Texture')
    ax.set_zlabel('Type')
    plt.title('cancer data')
    plt.legend()
    plt.show()




def p2():
    ins, outs = loadData2()
    insT, outsT, insV, outsV = prepareData2(ins, outs )
    yreal = [x[0]*0 + x[1]*1 + x[2] * 2 for x in outsV]

    #custom regressor
    regressor = LogisticRegressorMulti()
    regressor.fit(insT, outsT)
    
    ycomputed = []
    probs = regressor.predict(insV)
    for i in probs:
        ycomputed.append(argmax(i))

    acc = len([i for i in range(len(ycomputed)) if ycomputed[i] == yreal[i]])/len(ycomputed)
    print('custom regressor:')
    print(f'acc:{acc}')

    #tool regressor
    regressor_tool = sklearn.linear_model.LogisticRegression(multi_class = 'ovr')
    regressor_tool.fit(insT, [x[0]*0 + x[1] * 1 + x[2] * 2 for x in outsT])
    ycomputed = regressor_tool.predict(insV)
    
    acc = len([i for i in range(len(ycomputed)) if ycomputed[i] == yreal[i]])/len(ycomputed)
    print('tool regressor:')
    print(f'acc:{acc}')


def main():
    #Problema 1, cu cancerul 
    p1()    
    print('\n')
    #Problema 2, cu florile
    p2()


if __name__ == "__main__":
    main()
