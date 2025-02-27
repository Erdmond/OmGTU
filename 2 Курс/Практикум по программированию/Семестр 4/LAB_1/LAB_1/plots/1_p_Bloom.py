import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from LAB_1.algorythms.Bloom import *

def false_positive_rate(filter_size, hash_count, n):
    bloom = BloomFilter(filter_size, hash_count)
    dataset = list(range(1, n + 1))
    for num in dataset:
        bloom.add(str(num))
    false_positives = sum(str(num) in bloom for num in range(n + 1, 2 * n + 1))
    return false_positives / n


sizes = np.linspace(100, 5000, 10, dtype=int)
hash_counts = range(1, 11)
n = 500

data = []

plt.figure(figsize=(10, 6))
for hash_count in hash_counts:
    fpr_values = [false_positive_rate(size, hash_count, n) for size in sizes]
    plt.plot(sizes, fpr_values, label=f'Hash count: {hash_count}')
    for size, fpr in zip(sizes, fpr_values):
        data.append([size, hash_count, fpr])

plt.xlabel('Размер фильтра')
plt.ylabel('FPR (ложноположительные срабатывания)')
plt.title('Зависимость ложноположительных срабатываний от размера фильтра')
plt.legend()
plt.grid()
# plt.savefig('p_bloom_filter.png')
plt.show()

df = pd.DataFrame(data, columns=['size', 'number_of_hash', 'FPR'])
# df.to_csv('p_bloom_filter.csv', index=False, sep=';')
