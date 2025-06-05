import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances

class CustomKMeans:
    def __init__(self, n_clusters=3, max_iter=100, tol=1e-4, init='random', random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.init = init
        self.random_state = random_state
        self.centroids = None
        self.labels_ = None
        self.sse_ = None
        self.history_sse = []

    def _initialize_centroids(self, X):
        np.random.seed(self.random_state)
        if self.init == 'random':
            indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)
            return X[indices]
        elif self.init == 'k-means++':
            centroids = [X[np.random.randint(X.shape[0])]]
            for _ in range(1, self.n_clusters):
                dists = pairwise_distances(X, centroids, metric='euclidean')
                min_dists = np.min(dists, axis=1)
                probs = min_dists / min_dists.sum()
                centroid_idx = np.random.choice(X.shape[0], p=probs)
                centroids.append(X[centroid_idx])
            return np.array(centroids)
        else:
            raise ValueError("Invalid initialization method")

    def _calculate_sse(self, X, labels, centroids):
        return sum(np.linalg.norm(X[i] - centroids[labels[i]])**2 for i in range(X.shape[0]))

    def fit(self, X):
        X = X.values if isinstance(X, pd.DataFrame) else X
        
        self.centroids = self._initialize_centroids(X)
        
        for _ in range(self.max_iter):
            distances = pairwise_distances(X, self.centroids, metric='euclidean')
            self.labels_ = np.argmin(distances, axis=1)

            current_sse = self._calculate_sse(X, self.labels_, self.centroids)
            self.history_sse.append(current_sse)

            if len(self.history_sse) > 1:
                if abs(self.history_sse[-2] - current_sse) < self.tol:
                    break

            new_centroids = np.array([X[self.labels_ == k].mean(axis=0) 
                                    for k in range(self.n_clusters)])

            empty_clusters = np.isnan(new_centroids).any(axis=1)
            if empty_clusters.any():
                new_centroids[empty_clusters] = self._initialize_centroids(X)[empty_clusters]
            
            self.centroids = new_centroids
        
        self.sse_ = self.history_sse[-1]
        return self

    def predict(self, X):
        distances = pairwise_distances(X, self.centroids, metric='euclidean')
        return np.argmin(distances, axis=1)
