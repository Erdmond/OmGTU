import numpy as np

class SimpleKNN:
    def __init__(self, k=5):
        self.k = k  # количество соседей
    
    def fit(self, X, y):
        """Запоминаем обучающие данные"""
        self.X_train = np.array(X)
        self.y_train = np.array(y)
    
    def predict(self, X):
        """Предсказание для новых данных"""
        X = np.array(X)
        predictions = []
        
        for x in X:
            # 1. Вычисляем расстояния до всех точек
            distances = np.sqrt(np.sum((self.X_train - x)**2, axis=1))
            
            # 2. Находим k ближайших соседей
            nearest_indices = np.argsort(distances)[:self.k]
            nearest_labels = self.y_train[nearest_indices]
            
            # 3. Голосование большинством
            unique, counts = np.unique(nearest_labels, return_counts=True)
            winner = unique[np.argmax(counts)]
            predictions.append(winner)
            
        return np.array(predictions)
