
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
import random
import math
import sklearn.linear_model
import KMeans as kms
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.linear_model import SGDRegressor
import lab11
from sklearn.metrics import accuracy_score



def prepareData(ins, outs , ratio = 0.9):
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



def loadData():
    filename = 'iris.data'
    f = open(filename, 'r')
    
    ins = []
    outs = []

    for line in f.readlines():
        cols = line[:-1].split(",")
        ins.append([float(cols[0]), float(cols[1]), float(cols[2]), float(cols[3])])
        outs.append(cols[4])
    return ins, outs


def loadData1():
    filename = 'reviews_mixed.csv'
    f = open(filename, 'r')
    ins = []
    outs = []
    i = 0
    for line in f.readlines():
        if i == 0:
            i = 1
            continue
        else:
            words = line.split(',')
            outs.append(words[-1][:-1])
            ins.append(''.join(words[:-1]))

    return ins, outs

def prepareData1(ins, outs , ratio = 0.8):
    labels = []
    for x in outs:
        if x not in labels:
            labels.append(x)
    
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

def p():
    ins, outs = loadData()
    insT, outsT, insV, outsV = prepareData(ins, outs )
    yreal = [x[0]*0 + x[1]*1 + x[2] * 2 for x in outsV]

    #tool regressor
    regressor_tool = sklearn.linear_model.LogisticRegression(multi_class = 'ovr')
    regressor_tool.fit(insT, [x[0]*0 + x[1] * 1 + x[2] * 2 for x in outsT])
    ycomputed = regressor_tool.predict(insV)
    
    acc = len([i for i in range(len(ycomputed)) if ycomputed[i] == yreal[i]])/len(ycomputed)
    print('tool regressor:')
    print(f'acc:{acc}')

    kmeans = kms.KMeans(k=3)
    kmeans.fit(insT)
    print('Kmeans:')
    print(kmeans.predict(np.array(insV)))
    print('Real:')
    print([i for el in outsV for i in range(3) if el[i]==1])
    print('Tool:')
    print([x for x in ycomputed])

def p1():
    ins, outs = loadData1()
    insT, outsT, insV, outsV = prepareData1(ins, outs )

    labels = []
    for x in outs:
        if x not in labels:
            labels.append(x)
    
    vectorizer = CountVectorizer()
    
    trainFeatures = vectorizer.fit_transform(insT)
    outsT = [0 if outsT[i] == "positive" else 1 for i in range(len(outsT))]
    testFeatures = vectorizer.transform(insV)

    regressor = SGDRegressor(alpha=0.01,max_iter=1000)
    regressor.fit(trainFeatures,outsT)

    kmeans = KMeans(n_clusters=2, random_state=0)

    kmeans1 = kms.KMeans(k=2)

    kmeans.fit(trainFeatures)
    kmeans1.fit(trainFeatures.toarray())
    

    computed = regressor.predict(testFeatures)
    computed = [0 if computed[i] <0.5 else 1 for i in range(len(computed))]
    computed = [labels[value] for value in computed]
    print("regressor acc: ", accuracy_score(outsV, computed))
    
    computed = kmeans.predict(testFeatures)
    computed = [labels[value] for value in computed]
    print("kmeans tool acc: ", accuracy_score(outsV, computed))

    computed = kmeans1.predict(testFeatures.toarray())
    computed = [labels[value] for value in computed]
    print("kmeans acc: ", accuracy_score(outsV, computed))

def main():
    p()
    print('\n\n\n')
    p1()

if __name__ == "__main__":
    main()
