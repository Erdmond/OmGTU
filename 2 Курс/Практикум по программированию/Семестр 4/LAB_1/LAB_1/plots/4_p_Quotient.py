import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from LAB_1.algorythms.Quotient import *

def false_positive_rate_qf(size, n):
    qf = QuotientFilter(size)
    inserted = 0
    for num in range(1, n + 1):
        qf.insert(str(num))
        inserted += 1
    false_positives = sum(1 for num in range(n + 1, 2 * n + 1) if qf.lookup(str(num)))
    return false_positives / n, inserted


sizes = np.linspace(1000, 5000, 10, dtype=int)
n = 1000

data = []
fpr_values = []

plt.figure(figsize=(10, 6))
for size in sizes:
    fpr, inserted = false_positive_rate_qf(size, n)
    fpr_values.append(fpr)
    data.append([size, fpr, inserted])
    plt.plot(size, fpr, marker='o', color='b')

plt.plot(sizes, fpr_values, marker='o', linestyle='-', color='b')
plt.xlabel('Размер фильтра (size)')
plt.ylabel('Ложноположительный срабатывание (FPR)')
plt.title('Зависимость FPR QuotientFilter от размера фильтра')
plt.grid()
# plt.savefig('quotient_filter_fpr.png')
plt.show()

df = pd.DataFrame(data, columns=['Размер фильтра', 'FPR', 'Вставлено элементов'])
# df.to_csv('quotient_filter_fpr_data.csv', index=False)
