import optuna
from sklearn.metrics import silhouette_score
from typing import Tuple, Dict, Any, Type
import pandas as pd
from sklearn.base import BaseEstimator
import numpy as np

def optimize_clustering_hyperparameters(
    df: pd.DataFrame,
    model_class: Type[BaseEstimator],
    param_grid: Dict[str, Any],
    n_trials: int = 100,
    random_state: int = 42
) -> Tuple[float, Dict[str, Any]]:
    """
    Функция для подбора гиперпараметров алгоритмов кластеризации с использованием silhouette_score.
    
    Параметры:
    ----------
    df : pd.DataFrame
        Датафрейм с данными для кластеризации
    model_class : Type[BaseEstimator]
        Класс алгоритма кластеризации (KMeans, DBSCAN, AgglomerativeClustering и т.д.)
    param_grid : Dict[str, Any]
        Словарь с пространством поиска параметров для Optuna
    n_trials : int, optional
        Количество попыток оптимизации (по умолчанию 100)
    random_state : int, optional
        Seed для воспроизводимости (по умолчанию 42)
        
    Возвращает:
    -----------
    Tuple[float, Dict[str, Any]]
        Кортеж с лучшим значением silhouette_score и словарём лучших параметров
    """
    
    def objective(trial: optuna.Trial) -> float:
        """Внутренняя функция для Optuna, определяющая качество кластеризации."""
        params = {}

        for param_name, param_config in param_grid.items():
            if param_config['type'] == 'categorical':
                params[param_name] = trial.suggest_categorical(param_name, param_config['values'])
            elif param_config['type'] == 'int':
                params[param_name] = trial.suggest_int(
                    param_name, 
                    param_config['low'], 
                    param_config['high'], 
                    step=param_config.get('step', 1)
                )
            elif param_config['type'] == 'float':
                params[param_name] = trial.suggest_float(
                    param_name, 
                    param_config['low'], 
                    param_config['high'], 
                    step=param_config.get('step', None),
                    log=param_config.get('log', False)
                )

        model = model_class(**params)
        
        try:
            clusters = model.fit_predict(df)

            unique_clusters = np.unique(clusters)
            if len(unique_clusters) < 2 or (unique_clusters == -1).any():
                return -1

            score = silhouette_score(df, clusters)
            return score
        
        except Exception as e:
            return -1

    study = optuna.create_study(
        direction="maximize",
        sampler=optuna.samplers.TPESampler(seed=random_state)
    )

    study.optimize(objective, n_trials=n_trials, n_jobs=-1)

    return (study.best_value, study.best_params)
