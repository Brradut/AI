from utils import sigmoid


#folosim gradient descent pentru predictie
class LogisticRegressorMulti:
    def __init__(self):
        self.__weights = []
        self.__noLabels = 0

    
    def fit(self, x, y, learning_rate = 1, noEpochs = 1):
        self.__noLabels = len(y[0])
        self.__weights = [[0 for _ in range(len(y[0]))] for _ in range(len(x[0]) + 1)]

        for epoch in range(noEpochs):
            for i in range(len(x)):
                for p in range(self.__noLabels):
                    ycomputed = sigmoid(self.__weights[0][p] + sum([x[i][j-1] * self.__weights[j][p] for j in range(1, len(self.__weights))]))
                    error = ycomputed - y[i][p]
                    for j in range(0, len(x[0])):
                        self.__weights[j + 1][p] -= learning_rate * error * x[i][j]
                    self.__weights[0][p] -= learning_rate * error


    def predict(self, x):
        ycomputed =[]
        for i in range(len(x)):
            yy = []
            for p in range(self.__noLabels):
                yy.append(sigmoid(self.__weights[0][p] + sum([x[i][j-1] * self.__weights[j][p] for j in range(1, len(self.__weights))])))
            ycomputed.append(yy)
        return ycomputed


