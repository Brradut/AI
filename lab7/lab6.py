from math import sqrt
from math import log2
from math import exp
from math import log
def regressionError(computedOutputs, realOutputs):
    noSamples = 0
    L1=0
    L2=0
    for rowC, rowR in zip(computedOutputs, realOutputs):
        for c, r in zip(rowC, rowR):
            L1 += abs(r-c)  
            L2 += (r-c) ** 2
            noSamples = noSamples + 1
    L1 = L1/noSamples
    L2 = L2/noSamples
    L2 = sqrt(L2)

    return L1, L2

def classificationError(computedOutputs, realOutputs, pozLabel):
    noSample = len(computedOutputs)
    TP=0
    FP=0
    TN=0
    FN=0
    for r, c in zip(computedOutputs, realOutputs):
        if r == c and c == pozLabel:
            TP+=1
        if r ==c and c != pozLabel:
            TN+=1
        if r!=c and c == pozLabel:
            FP+=1
        if r!=c and c != pozLabel:
            FN+=1
    acc = (TP + TN)/(TP + TN + FP + FN)
    preciziePoz = TP / (TP + FP)
    rapelPoz = TP / (TP + FN)
    precizieNeg = TN / (TN + FN)
    rapelNeg = TN / (TN + FP)
    return acc, [preciziePoz, precizieNeg], [rapelPoz, rapelNeg]

def crossEntropy(p, q):
    s = 0
    for pi, qi in zip(p, q):
        s = s - pi * log2(qi)
    return s

def sigmoid(x):
    return 1 / (1 + exp(-x))

def softmax(output):
    s = sum(output)
    return [e/s for e in output]
    
    
def lossClassificationBinary(computedOutputs, realOutputs, label):
    nrOutputs=0
    m=0
    for c, r in zip(computedOutputs, realOutputs):
        p = [0] * 2
        if r == label:
            p = [0, 1]
        else:
            p = [1, 0]
        q = [1-c, c]
        m = m + crossEntropy(p, q)
        nrOutputs = nrOutputs + 1
    return m / nrOutputs

def lossClassificationMultiClass(computedOutputs, realOutputs, labels):
    labelPosition = {}
    nrLabels = 0
    for l in labels:
        labelPosition[l]=nrLabels
        nrLabels = nrLabels + 1
    nrOutputs=0
    m=0
    for c, r in zip(computedOutputs, realOutputs):
        p = [0] * nrLabels
        p[labelPosition[r]]=1
        q = softmax(c)
        m = m + crossEntropy(p, q)
        nrOutputs = nrOutputs + 1
    return m / nrOutputs



def lossClassificationMultiLabel(computedOutputs, realOutputs, labels):
    labelPosition = {}
    nrLabels = 0
    for l in labels:
        labelPosition[l]=nrLabels
        nrLabels = nrLabels + 1
    m=0
    nrOutputs=0
    for c, r in zip(computedOutputs, realOutputs):
        p = [0] * nrLabels
        for l in r:
            p[labelPosition[l]]=1
        q = c
        m = m + sum([-pi * log(qi) -(1-pi)*log(1-qi) for pi, qi in zip(p, q)])
        nrOutputs = nrOutputs + 1
    return m/nrOutputs

def main():
    computedReggresion = [[2, 7, 4.5, 6, 3, 8, 3, 1.2]]
    realRegression = [[3, 9.5, 4, 5.1, 6, 7.2, 2, 1]]
    computedClassification = ['infected', 'infected', 'normal', 'normal', 'normal', 'normal','normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'infected']
    realClassification =  ['infected', 'infected', 'infected', 'infected', 'normal', 'normal', 'normal', 'normal', 'normal','normal', 'normal', 'normal', 'normal', 'normal', 'normal']

    print(regressionError(computedReggresion, realRegression))
    print(classificationError(computedClassification, realClassification, 'infected'))

    print(lossClassificationBinary([0.9, 0.8, 0.4, 0.3, 0.3, 0.2, 0.4, 0.1, 0.5, 0.5, 0.4, 0.3, 0.2, 0.1, 0.7], realClassification, 'infected'))
    print(lossClassificationMultiClass([[0.9, 0.1], [0.8, 0.2], [0.4, 0.6], [0.3, 0.7], [0.3, 0.7], [0.2, 0.8], [0.4, 0.6], [0.1, 0.9], [0.5, 0.5], [0.5, 0.5], [0.4, 0.6], [0.3, 0.7], [0.2, 0.8], [0.1, 0.9], [0.7, 0.3]], realClassification, ['infected', 'normal']))
    print(lossClassificationMultiLabel([[0.9, 0.1], [0.8, 0.2], [0.4, 0.6], [0.3, 0.7], [0.3, 0.7], [0.2, 0.8], [0.4, 0.6], [0.1, 0.9], [0.5, 0.5], [0.5, 0.5], [0.4, 0.6], [0.3, 0.7], [0.2, 0.8], [0.1, 0.9], [0.7, 0.3]], [[e] for e in realClassification], ['infected', 'normal']))
