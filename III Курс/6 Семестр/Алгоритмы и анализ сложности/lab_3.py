from analisys.funcs import *

def narayana(n):
    a = list(range(1, n + 1))
    yield a.copy()
    while True:
        i = n - 2
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1
        if i < 0:
            return
        j = n - 1
        while a[j] <= a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
        a[i + 1:] = reversed(a[i + 1:])
        yield a.copy()


def johnson_trotter(n):
    a = list(range(1, n + 1))
    d = [-1] * n
    yield a.copy()
    while True:
        mobile = -1
        idx = -1
        for i in range(n):
            j = i + d[i]
            if 0 <= j < n and a[i] > a[j] and a[i] > mobile:
                mobile = a[i]
                idx = i
        if mobile == -1:
            return
        j = idx + d[idx]
        a[idx], a[j] = a[j], a[idx]
        d[idx], d[j] = d[j], d[idx]
        for i in range(n):
            if a[i] > mobile:
                d[i] *= -1
        yield a.copy()


def inversion_vector(n):
    def gen(inv, k):
        if k == n:
            yield inv.copy()
        else:
            for i in range(k + 1):
                inv[k] = i
                yield from gen(inv, k + 1)

    for inv in gen([0] * n, 0):
        perm = []
        for i in reversed(range(n)):
            perm.insert(inv[i], i + 1)
        yield perm


def permute_list(seq):
    for p in narayana(len(seq)):
        yield [seq[i - 1] for i in p]


def unique_permutations(seq):
    seen = set()
    for p in permute_list(seq):
        t = tuple(p)
        if t not in seen:
            seen.add(t)
            yield p


def all_subsets(elements):
    n = len(elements)
    base = list(range(n))
    subsets = set()
    for r in range(1, n + 1):
        for p in narayana(n):
            subset = tuple(sorted(elements[i - 1] for i in p[:r]))
            subsets.add(subset)
    for s in subsets:
        yield s


def max_items(budget, wishlist, price_list):
    items = []
    for name, qty in wishlist.items():
        if name in price_list:
            for _ in range(qty):
                items.append((name, price_list[name]))

    best = {}
    max_count = 0

    for p in permute_list(items):
        total = 0
        current = {}
        for name, price in p:
            if total + price <= budget:
                total += price
                current[name] = current.get(name, 0) + 1
        count = sum(current.values())
        if count > max_count:
            max_count = count
            best = current

    return best

if __name__=='__main__':
    print("\nЗадание 1.")

    ns = list(range(1, 11))
    algorithms = {
        "Нарайана": narayana,
        "Джонсон-Троттер": johnson_trotter,
        "Вектор инверсий": inversion_vector
    }

    time_data = {name: [] for name in algorithms}

    for n in ns:
        print(f"\nn = {n}")
        for name, func in algorithms.items():
            elapsed, result = measure_time(lambda f, k: list(f(k)), func, n)
            time_data[name].append(elapsed)
            print(f"{name}: {len(result)} перестановок | {elapsed:.6f} сек")

    plot_results(
        x_values=ns,
        times_dict=time_data,
        title="Сравнение алгоритмов генерации перестановок",
        x_label="n",
        y_label="Время выполнения (сек)"
    )


    print("\nЗадание 2.")

    for seq in [[1, 2, 1], [1, 2, 3]]:
        print("\nПоследовательность:", seq)
        for p in unique_permutations(seq):
            print(p)


    print("\nЗадание 3.")

    elements = ["стол", "стул", "шкаф"]
    for s in all_subsets(elements):
        print(s)


    print("\nЗадание 4.")

    wishlist = {"ручка": 3, "тетрадь": 2, "карандаш": 5}
    price_list = {"ручка": 10, "тетрадь": 25, "карандаш": 5}
    budget = 100

    result = max_items(budget, wishlist, price_list)

    print("Бюджет:", budget)
    print("Можно купить:")
    for name, qty in result.items():
        print(f"{name} – {qty}")
