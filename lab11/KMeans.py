import numpy as np
import matplotlib.pyplot as plt
import random


def distance(x, y):
    return np.sqrt(np.sum((x - y)**2, axis=1))


class KMeans:
    def __init__(self, k=2, max_iter=100):
        self.k =k
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, x):
        self.centroids = [random.choice(x)]
        for _ in range(self.k-1):

            d = np.sum([distance(centroid, x) for centroid in self.centroids], axis=0)
            d = d / np.sum(d)

            a, = np.random.choice(range(len(x)), size=1, p=d)
            self.centroids += [x[a]]
        iteration = 0
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and iteration < self.max_iter:

            sorted_points = [[] for _ in range(self.k)]

            for i in x:
                d = distance(i, self.centroids)
                a= np.argmin(d)
                sorted_points[a].append(i)

            prev_centroids = self.centroids 
            self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
            iteration += 1
    def predict(self, x):
        cs = []
        for i in x:
            d = distance(i, self.centroids)
            c = np.argmin(d)
            cs.append(c)
        return cs
