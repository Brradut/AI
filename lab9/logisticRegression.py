from utils import sigmoid


#folosim gradient descent pentru predictie
class LogisticRegressor:
    def __init__(self):
        self.__weights = []

    
    def fit(self, x, y, learning_rate = 1, noEpochs = 1):
        self.__weights = [0 for _ in range(len(x[0]) + 1)]

        for epoch in range(noEpochs):
            for i in range(len(x)):
                ycomputed = sigmoid(self.__weights[0] + sum([x[i][j-1] * self.__weights[j] for j in range(1, len(self.__weights))]))
                error = ycomputed - y[i]
                for j in range(0, len(x[0])):
                    self.__weights[j + 1] -= learning_rate * error * x[i][j]
                self.__weights[0] -= learning_rate * error


    def predict(self, x):
        ycomputed =[]
        for i in range(len(x)):
            ycomputed.append(sigmoid(self.__weights[0] + sum([x[i][j-1] * self.__weights[j] for j in range(1, len(self.__weights))])))
        return ycomputed


