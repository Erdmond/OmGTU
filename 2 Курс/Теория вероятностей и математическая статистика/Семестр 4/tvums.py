import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import math

# ввод данных
data = list(map(float, list('35433323333240333312332252441231403564822510153251')))
print(len(data))

# создание вариационного ряда
variational_series = sorted(data)
print("Вариационный ряд: ", end='')
print(*variational_series)

plot_data = np.array(sorted(list(map(int, data))))
n = len(plot_data)
unique_vals = np.sort(np.unique(plot_data))
F_values = np.array([np.sum(plot_data <= x) / n for x in unique_vals])
plt.figure(figsize=(8, 5))
for i, x in enumerate(unique_vals):
    if i == 0:
        x_start = x
    else:
        x_start = unique_vals[i - 1]
    x_end = x
    plt.hlines(F_values[i], x_start, x_end, colors='blue', lw=2)
    if x!=0:
        plt.annotate('', xy=(x_start, F_values[i]), xytext=(x_start + 0.01, F_values[i]),
                     arrowprops=dict(arrowstyle='->', color='blue', lw=2))

# Отображаем последнюю точку, чтобы подчеркнуть уровень функции в конце
plt.plot(unique_vals[-1], F_values[-1], 'bo')

plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Эмпирическая функция распределения')
plt.grid(True)
plt.show()

# вычисление характеристик
info_data = np.array(data)
print("Числовые характеристики выборки:")
print(f"Выборочное среднее: {np.mean(info_data):.3f}")
print(f"Исправленная выборочная дисперсия: {np.var(info_data, ddof=1):.3f}")
print(f"Медиана: {np.median(info_data)}")
print(f"Мода: {stats.mode(info_data, keepdims=True).mode[0]}")
print(f"Асимметрия: {stats.skew(info_data, bias=False):.3f}")
print(f"Эксцесс: {stats.kurtosis(info_data, bias=False):.3f}")

n = len(data)
x_min = min(data)
x_max = max(data)
h = (x_max - x_min) / (1 + 3.322 * math.log10(n))
k = int(np.ceil((x_max - x_min) / h))
x0 = x_min - h/2
xk = x_max + h/2
bins = np.linspace(x0, xk, k + 1)
# построение интервального статистического ряда
# Рассчитываем абсолютные частоты по вычисленным интервалам
freq, bin_edges = np.histogram(data, bins=bins)
# Вычисляем относительные частоты
rel_freq = freq / n
# Формирование таблицы интервального статистического ряда
interval_labels = [f"[{bin_edges[i]:.3f}, {bin_edges[i+1]:.3f})" for i in range(len(freq))]
interval_table = pd.DataFrame({
    'Интервал': interval_labels,
    'Частота': freq,
    'Относительная частота': rel_freq
})
print("Интервальный статистический ряд:")
print(interval_table)

# построение полигона и гистограммы относительных частот
# Центры интервалов рассчитываются как среднее между соседними границами
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
plt.figure(figsize=(12, 5))
# Полигон относительных частот
plt.subplot(1, 2, 1)
plt.plot(bin_centers, rel_freq, marker='o', linestyle='-', color='blue')
plt.xlabel('Значение')
plt.ylabel('Относительная частота')
plt.title('Полигон относительных частот')
plt.grid(True)
# Гистограмма относительных частот
plt.subplot(1, 2, 2)
plt.bar(bin_centers, rel_freq, width=h*0.9, edgecolor='black', color='lightgreen', align='center')
plt.xlabel('Значение')
plt.ylabel('Относительная частота')
plt.title('Гистограмма относительных частот')
plt.grid(True)
plt.tight_layout()
plt.show()
