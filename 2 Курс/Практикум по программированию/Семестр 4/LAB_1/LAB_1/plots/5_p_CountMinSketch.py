import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from LAB_1.algorythms.CountMinSketch import *

def false_positive_rate_cms(width, depth, n):
    cms = CountMinSketch(width, depth)
    for num in range(1, n + 1):
        cms.add(str(num))
    false_positives = sum(1 for num in range(n + 1, 2 * n + 1) if cms.estimate(str(num)) > 0)
    return false_positives / n


widths = np.linspace(100, 3000, 10, dtype=int)
depths = range(1, 11)
n = 500

data = []
plt.figure(figsize=(12, 8))

for depth in depths:
    fpr_values = []
    for width in widths:
        fpr = false_positive_rate_cms(width, depth, n)
        fpr_values.append(fpr)
        data.append([width, depth, fpr])
    plt.plot(widths, fpr_values, marker='o', label=f'Глубина: {depth}')

plt.xlabel('Ширина (width)')
plt.ylabel('Ложноположительный срабатывание (FPR)')
plt.title('Зависимость FPR CountMinSketch от ширины и глубины')
plt.legend(title='Глубина')
plt.grid()
# plt.savefig('count_min_sketch_fpr.png')
plt.show()

df = pd.DataFrame(data, columns=['Ширина', 'Глубина', 'FPR'])
# df.to_csv('count_min_sketch_fpr_data.csv', index=False)
