from analisys.funcs import *
from lab_3 import narayana, johnson_trotter, inversion_vector

def gray_permutations(n):
    if n == 1:
        yield [1]
        return
    prev = list(gray_permutations(n - 1))
    for i, p in enumerate(prev):
        if i % 2 == 0:
            for j in range(n):
                yield p[:j] + [n] + p[j:]
        else:
            for j in reversed(range(n)):
                yield p[:j] + [n] + p[j:]


def heap_permutations(n):
    a = list(range(1, n + 1))
    c = [0] * n
    yield a.copy()
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                a[0], a[i] = a[i], a[0]
            else:
                a[c[i]], a[i] = a[i], a[c[i]]
            yield a.copy()
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1


ns = list(range(1, 11))

algorithms = {
    "Нарайана": narayana,
    "Джонсон-Троттер": johnson_trotter,
    "Вектор инверсий": inversion_vector,
    "Код Грэя": gray_permutations,
    "Алгоритм Хипа": heap_permutations
}

time_data = {name: [] for name in algorithms}
gray_data = {}

for n in ns:
    print(f"\nn = {n}")
    for name, func in algorithms.items():
        elapsed, result = measure_time(lambda f, k: list(f(k)), func, n)
        time_data[name].append(elapsed)
        if name == 'Код Грэя' and n < 6:
            gray_data[n] = result
        print(f"{name:20} | {len(result)} перестановок | {elapsed:.6f} сек")

print('\n'.join([f'{n}: {data}' for n, data in list(gray_data.items())]))

plot_results(
    x_values=ns,
    times_dict=time_data,
    title="Сравнение алгоритмов генерации перестановок",
    x_label="n",
    y_label="Время выполнения (сек)"
)
