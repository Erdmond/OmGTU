import matplotlib.pyplot as plt
import pandas as pd
from LAB_1.algorythms.MinHash import *

def false_positive_rate_minhash(num_hashes, set_size):
    set1 = set(range(set_size))
    set2 = set(range(set_size, 2 * set_size))
    set1_list = list(set1)
    set2_list = list(set2)
    minhash = MinHash(num_hashes=num_hashes)
    similarity = minhash.compute_similarity(set1_list, set2_list)
    return similarity

num_hashes_values = range(10, 110, 10)
set_size = 500

data = []
similarities = []

plt.figure(figsize=(10, 6))
for num_hashes in num_hashes_values:
    sim = false_positive_rate_minhash(num_hashes, set_size)
    similarities.append(sim)
    data.append([num_hashes, sim])

plt.plot(list(num_hashes_values), similarities, marker='o')
plt.xlabel('Количество хеш-функций (num_hashes)')
plt.ylabel('Ложноположительная схожесть')
plt.title('Зависимость ложноположительной схожести от количества хеш-функций (MinHash)')
plt.grid()
# plt.savefig('minhash_false_positive.png')
plt.show()

df = pd.DataFrame(data, columns=['Количество хеш-функций', 'Ложноположительная схожесть'])
# df.to_csv('minhash_false_positive_data.csv', index=False, sep=';')
