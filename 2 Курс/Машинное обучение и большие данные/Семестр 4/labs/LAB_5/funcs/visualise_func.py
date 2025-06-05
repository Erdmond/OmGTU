import matplotlib.pyplot as plt
from typing import Union, List
import seaborn as sns
import pandas as pd
import numpy as np

def plot_cluster_analysis(
    df: pd.DataFrame,
    target_col: Union[str, pd.Series, np.ndarray],
    feature_cols: List[str] = None,
    figsize: tuple = (18, 7),
    palette: str = 'crest',
    alpha: float = 0.8,
    point_size: int = 100,
    bw_method: float = 0.2
) -> None:
    """
    Визуализация кластеров через scatter plot и violin plot с одинаковым масштабом.
    
    Параметры:
    ----------
    df : pd.DataFrame
        Исходный датафрейм с данными
    target_col : str, pd.Series или np.ndarray
        Столбец с метками классов/кластеров или массив меток
    feature_cols : list, optional
        Список из 2 признаков для осей графиков (по умолчанию первые 2 числовых столбца)
    figsize : tuple, optional
        Размер фигуры (ширина, высота)
    palette : str, optional
        Цветовая палитра (из seaborn)
    alpha : float, optional
        Прозрачность точек (0-1)
    point_size : int, optional
        Размер точек в scatter plot
    bw_method : float, optional
        Параметр сглаживания для violin plot (0.1-0.5)
    """
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.facecolor'] = 'white'

    df_vis = df.copy()

    if not isinstance(target_col, str):
        df_vis['Cluster'] = target_col
        target_col = 'Cluster'

    if feature_cols is None:
        numeric_cols = df_vis.select_dtypes(include=['number']).columns.tolist()
        feature_cols = numeric_cols[:2]
        if len(feature_cols) < 2:
            raise ValueError("В датафрейме должно быть хотя бы 2 числовых столбца")

    for col in feature_cols + [target_col]:
        if col not in df_vis.columns:
            raise ValueError(f"Столбец '{col}' не найден в датафрейме")

    y_min = min(df_vis[feature_cols[0]].min(), df_vis[feature_cols[1]].min()) * 1.1
    y_max = max(df_vis[feature_cols[0]].max(), df_vis[feature_cols[1]].max()) * 1.1

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

    sns.scatterplot(
        data=df_vis,
        x=feature_cols[0],
        y=feature_cols[1],
        hue=target_col,
        palette=palette,
        alpha=alpha,
        s=point_size,
        edgecolor='w',
        linewidth=0.5,
        ax=ax1
    )
    ax1.set_title(f'Scatter: {feature_cols[0]} vs {feature_cols[1]}', pad=15)
    ax1.legend(title='Class', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.set_ylim(y_min, y_max)

    sns.violinplot(
        data=df_vis,
        x=target_col,
        y=feature_cols[1],
        hue=target_col,
        palette=palette,
        inner='quartile',
        bw_method=bw_method,
        cut=1,
        ax=ax2,
        legend=False
    )
    ax2.set_title(f'Violin Plot', pad=15)
    ax2.set_xlabel('Class')
    ax2.grid(True, linestyle=':', alpha=0.7)
    ax2.set_ylim(y_min, y_max)
    
    plt.tight_layout()
    plt.show()

    g = sns.jointplot(
        data=df_vis,
        x=feature_cols[0],
        y=feature_cols[1],
        hue=target_col,
        palette=palette)
    g.plot_joint(
        sns.kdeplot,
        color="r",
        zorder=0,
        levels=6,
        alpha=0.3,
        palette=palette)
    plt.legend(title='Class')
    plt.show()
