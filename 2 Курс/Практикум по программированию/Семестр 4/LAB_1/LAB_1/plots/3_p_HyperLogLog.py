import matplotlib.pyplot as plt
import pandas as pd
from LAB_1.algorythms.HyperLogLog import *

def false_positive_rate_hyperloglog(precision, set_size):
    test_set = set(range(set_size))
    hll = HyperLogLog(precision=precision)
    for value in test_set:
        hll.add(value)
    estimated_count = hll.estimate()
    true_count = len(test_set)
    deviation_percent = (abs(estimated_count - true_count) / true_count) * 100
    return deviation_percent


set_size = 100000

data = []
deviations = []

plt.figure(figsize=(10, 6))
for precision in range(4, 17):
    deviation = false_positive_rate_hyperloglog(precision, set_size)
    deviations.append(deviation)
    data.append([precision, deviation])

plt.plot(range(4, 17), deviations, marker='o')
plt.xlabel('Точность (precision)')
plt.ylabel('Процент отклонения от реального количества элементов')
plt.title('Отклонение оценки HyperLogLog от реального количества элементов в зависимости от точности')
plt.grid()
# plt.savefig('hyperloglog_deviation_precision.png')
plt.show()

df = pd.DataFrame(data, columns=['Точность (precision)', 'Процент отклонения'])
# df.to_csv('hyperloglog_deviation_precision_data.csv', index=False, sep=';')