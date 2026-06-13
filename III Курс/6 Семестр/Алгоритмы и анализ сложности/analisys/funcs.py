import matplotlib.pyplot as plt
import time

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    return (time.time() - start, result)


def plot_results(x_values, times_dict, title="", x_label="", y_label="Время выполнения (сек)"):
    fig, ax = plt.subplots()
    
    for label, times in times_dict.items():
        ax.plot(x_values, times, label=label)
    
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    if title:
        ax.set_title(title)
    
    if len(times_dict) > 1:
        ax.legend()
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
