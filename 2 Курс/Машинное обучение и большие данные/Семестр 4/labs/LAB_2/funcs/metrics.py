import numpy as np

def MAE(y_true, y_pred):
    """
    Средняя абсолютная ошибка (MAE)
    MAE = (1/m) * Σ |y_true - y_pred|
    """
    return np.mean(np.abs(y_true - y_pred))

def MSE(y_true, y_pred):
    """
    Среднеквадратичная ошибка (MSE)
    MSE = (1/m) * Σ (y_true - y_pred)^2
    """
    return np.mean((y_true - y_pred)**2)

def RMSE(y_true, y_pred):
    """
    Корень из среднеквадратичной ошибки (RMSE)
    RMSE = sqrt(MSE)
    """
    return np.sqrt(MSE(y_true, y_pred))

def MAPE(y_true, y_pred):
    """
    Средняя абсолютная процентная ошибка (MAPE)
    MAPE = (1/m) * Σ |(y_true - y_pred) / y_true| * 100
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    nonzero_idx = y_true != 0
    return np.mean(np.abs((y_true[nonzero_idx] - y_pred[nonzero_idx]) / y_true[nonzero_idx]))

def R2(y_true, y_pred):
    """
    Коэффициент детерминации (R²)
    R² = 1 - (SS_res / SS_tot),
    где SS_res = Σ (y_true - y_pred)² и SS_tot = Σ (y_true - mean(y_true))².
    """
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - ss_res/ss_tot
