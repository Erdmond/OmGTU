import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from LAB_1.algorythms.CountingBloom import *

def false_positive_rate_add_remove(filter_size, hash_count, n):
    bloom = CountingBloomFilter(filter_size, hash_count)
    dataset = list(range(1, n + 1))
    for num in dataset:
        bloom.add(str(num))
    for num in dataset[:n // 2]:
        bloom.remove(str(num))
    false_positives = sum(str(num) in bloom for num in range(n + 1, 2 * n + 1))
    return false_positives / n

sizes = np.linspace(100, 5000, 10, dtype=int)
hash_counts = range(1, 11)
n = 500

data = []

plt.figure(figsize=(10, 6))
for hash_count in hash_counts:
    fpr_values = [false_positive_rate_add_remove(size, hash_count, n) for size in sizes]
    plt.plot(sizes, fpr_values, label=f'Hash count: {hash_count}')
    for size, fpr in zip(sizes, fpr_values):
        data.append([size, hash_count, fpr])

plt.xlabel('Размер фильтра')
plt.ylabel('FPR (ложноположительные срабатывания) после удаления элементов')
plt.title('Зависимость FPR от размера фильтра (Counting Bloom Filter)')
plt.legend()
plt.grid()
plt.savefig('counting_bloom_filter_fpr.png')
plt.show()

df = pd.DataFrame(data, columns=['Размер фильтра', 'Кол-во хеш-функций', 'FPR'])
df.to_csv('counting_bloom_filter_fpr_data.csv', index=False, sep=';')
