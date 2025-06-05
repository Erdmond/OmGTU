from itertools import combinations
import matplotlib.pyplot as plt
from math import ceil
import numpy as np

def plot_scatter(
    X, 
    y, 
    point_size=20, 
    alpha=0.7, 
    palette='viridis',
    max_plots_per_figure=16,
    plots_per_row=4,
):
    if hasattr(X, 'columns'):
        feature_names = X.columns.tolist()
        X = np.array(X)
    else:
        feature_names = [f'Feature {i}' for i in range(X.shape[1])]
        X = np.array(X)
    
    y = np.array(y)
    n_features = X.shape[1]
    
    if n_features <= 2:
        plt.figure(figsize=(8, 6))
        if n_features == 2:
            scatter = plt.scatter(X[:, 0], X[:, 1], c=y, s=point_size, alpha=alpha, cmap=palette)
        else:
            scatter = plt.scatter(X[:, 0], np.zeros_like(X[:, 0]), c=y, s=point_size, alpha=alpha, cmap=palette)
        plt.xlabel(feature_names[0])
        plt.ylabel(feature_names[1] if n_features == 2 else '')
        plt.colorbar(scatter)
        plt.tight_layout()
        plt.show()
        return
    
    feature_pairs = list(combinations(range(n_features), 2))
    n_pairs = len(feature_pairs)
    n_figures = ceil(n_pairs / max_plots_per_figure)
    
    for fig_num in range(n_figures):
        start_idx = fig_num * max_plots_per_figure
        end_idx = min((fig_num + 1) * max_plots_per_figure, n_pairs)
        current_pairs = feature_pairs[start_idx:end_idx]
        n_current = len(current_pairs)
        n_rows = ceil(n_current / plots_per_row)
        
        fig, axes = plt.subplots(n_rows, plots_per_row, 
                               figsize=(5*plots_per_row, 5*n_rows),
                               squeeze=False)
        axes = axes.flatten()
        
        for ax_idx, (j, k) in enumerate(current_pairs):
            ax = axes[ax_idx]
            scatter = ax.scatter(X[:, j], X[:, k], c=y, s=point_size, alpha=alpha, cmap=palette)
            ax.set_xlabel(feature_names[j])
            ax.set_ylabel(feature_names[k])
            fig.colorbar(scatter, ax=ax)
        
        for ax in axes[n_current:]:
            ax.set_visible(False)
        
        plt.tight_layout()
        plt.show()
