from math import sqrt
from math import log2
from math import exp
from math import log


def regressionError(computedOutputs, realOutputs):
    noSamples = len(computedOutputs[0])
    L1=0    #mean absolute error
    L2=0    #root mean square error
    for rowC, rowR in zip(computedOutputs, realOutputs):
        for c, r in zip(rowC, rowR):
            L1 += abs(r-c)  
            L2 += (r-c) ** 2
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
        if r == c and c != pozLabel:
            TN+=1
        if r != c and c == pozLabel:
            FP+=1
        if r != c and c != pozLabel:
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

def readData():
    filename1 = 'flowers.csv'
    filename2 = 'sport.csv'
    
    file1 = open(filename1)
    file2 = open(filename2)
    
    #reading data for flowers
    realOutputsFlowers = []
    computedOutputsFlowers = []

    for line in file1.readlines()[1:]:
        r, c = line[:-1].split(",")
        computedOutputsFlowers.append(c)
        realOutputsFlowers.append(r)
    
    #reading data for sport
    realOutputsSport = []
    computedOutputsSport = []

    for line in file2.readlines()[1:]:
        r1, r2, r3, c1, c2, c3 = line[:-1].split(',')
        computedOutputsSport.append([int(c1),int(c2),int(c3)])
        realOutputsSport.append([int(r1), int(r2), int(r3)])

    return realOutputsFlowers, computedOutputsFlowers, realOutputsSport, computedOutputsSport


def main():
    realOutputsFlowers, computedOutputsFlowers, realOutputsSport, computedOutputsSport = readData()
    
    MAE, RMSE = regressionError(computedOutputsSport, realOutputsSport)
    print(f"MAE: {MAE}, RMSE: {RMSE} for sport.csv")
    
    acc, precizie, rapel = classificationError(computedOutputsFlowers, realOutputsFlowers, 'Daisy')
    print(f'Accuracy: {acc}, Precision: {precizie}, Recall: {rapel} for Daisy')
    acc, precizie, rapel = classificationError(computedOutputsFlowers, realOutputsFlowers, 'Rose')
    print(f'Accuracy: {acc}, Precision: {precizie}, Recall: {rapel} for Rose')
    acc, precizie, rapel = classificationError(computedOutputsFlowers, realOutputsFlowers, 'Tulip')
    print(f'Accuracy: {acc}, Precision: {precizie}, Recall: {rapel} for Tulip')

    realOutputs = [[7.53], [7.52], [7.5], [7.49], [7.46]]
    computedOutputs = [[7.8], [7.75], [7.45], [7.6], [7.4]]
    MAE, RMSE = regressionError(computedOutputs, realOutputs)
    print(f"Loss regression. MAE: {MAE}, RMSE:{RMSE}")

    computedClassification = ['infected', 'infected', 'normal', 'normal', 'normal', 'normal','normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'infected']
    realClassification =  ['infected', 'infected', 'infected', 'infected', 'normal', 'normal', 'normal', 'normal', 'normal','normal', 'normal', 'normal', 'normal', 'normal', 'normal']
    
    error = lossClassificationBinary([0.9, 0.8, 0.4, 0.3, 0.3, 0.2, 0.4, 0.1, 0.5, 0.5, 0.4, 0.3, 0.2, 0.1, 0.7], realClassification, 'infected')
    print(f'Loss binary classification: {error}')
    error = lossClassificationMultiClass([[0.9, 0.1], [0.8, 0.2], [0.4, 0.6], [0.3, 0.7], [0.3, 0.7], [0.2, 0.8], [0.4, 0.6], [0.1, 0.9], [0.5, 0.5], [0.5, 0.5], [0.4, 0.6], [0.3, 0.7], [0.2, 0.8], [0.1, 0.9], [0.7, 0.3]], realClassification, ['infected', 'normal'])
    print(f'Loss multi class classification: {error}')
    error = lossClassificationMultiLabel([[0.9, 0.1], [0.8, 0.2], [0.4, 0.6], [0.3, 0.7], [0.3, 0.7], [0.2, 0.8], [0.4, 0.6], [0.1, 0.9], [0.5, 0.5], [0.5, 0.5], [0.4, 0.6], [0.3, 0.7], [0.2, 0.8], [0.1, 0.9], [0.7, 0.3]], [[e] for e in realClassification], ['infected', 'normal'])
    print(f'Loss multi label classification: {error}')

if __name__ == "__main__":
    main()
