import numpy
import utils
#b = ((X'*X)^-1)*X' * y

class ToolLinearRegressor:
    def __init__(self):
        self.__weights =[]
   
    def fit(self, x, y):
        X = [[i for i in e] for e in x]
        for e in X:
            e.insert(0, 1) # pentru termenul liber
        X = numpy.array(X)
        Y = numpy.array([e for e in y])
        t = numpy.linalg.inv(numpy.matmul(X.transpose(), X)) # (X'X)^-1
        p = numpy.matmul(t, X.transpose()) # * X'
        w = numpy.matmul(p, Y) # * y
        self.__weights = w
    
    def predict(self, x):
        sum = 0
        index = 0
        while index < len(x):
            sum = sum + x[index] * self.__weights[index+1]
            index = index + 1
        sum += self.__weights[0]
        return sum

class CustomLinearRegressor:
    def __init__(self):
        self.__weights = []

    def fit(self, x, y):
        X = [[i for i in e] for e in x]
        for e in X:
            e.insert(0, 1) # pentru termenul liber
        Y = [e for e in y]
        t = utils.inv(utils.matmul(utils.transpose(X), X)) # (X'X)^-1
        p = utils.matmul(t, utils.transpose(X))# * X'
        w = utils.matmul(p, Y) # * y
        self.__weights = utils.transpose(w)[0]

    def predict(self, x):
        s = 0
        index = 0
        while index < len(x):
            s = s + x[index] * self.__weights[index + 1]
            index = index + 1
        s += self.__weights[0]
        return [s]
