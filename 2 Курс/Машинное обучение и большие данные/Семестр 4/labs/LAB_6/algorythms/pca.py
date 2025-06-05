import numpy as np

class CustomPCA:
    def __init__(self, n_components=None, whiten=False):
        self.n_components = n_components
        self.whiten = whiten
        self.mean_ = None
        self.components_ = None
        self.explained_variance_ = None
        self.explained_variance_ratio_ = None
    
    def fit(self, X):
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

        cov_matrix = np.cov(X_centered, rowvar=False)

        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

        sorted_idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[sorted_idx]
        eigenvectors = eigenvectors[:, sorted_idx]

        if self.n_components is None:
            self.n_components = X.shape[1]
        elif 0 < self.n_components < 1:
            total_variance = np.sum(eigenvalues)
            cumulative_variance = np.cumsum(eigenvalues) / total_variance
            self.n_components = np.argmax(cumulative_variance >= self.n_components) + 1

        self.components_ = eigenvectors[:, :self.n_components].T
        self.explained_variance_ = eigenvalues[:self.n_components]
        self.explained_variance_ratio_ = self.explained_variance_ / np.sum(eigenvalues)
        
        return self
    
    def transform(self, X):
        X_centered = X - self.mean_
        X_transformed = np.dot(X_centered, self.components_.T)

        if self.whiten:
            X_transformed /= np.sqrt(self.explained_variance_ + 1e-6)
            
        return X_transformed
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
