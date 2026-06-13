from analisys.funcs import *

def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1


def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    bad = {}
    for i in range(m - 1):
        bad[pattern[i]] = m - 1 - i

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        shift = bad.get(text[i + m - 1], m)
        i += shift
    return -1


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    base = 256
    mod = 101

    hpattern = 0
    htext = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % mod
        htext = (base * htext + ord(text[i])) % mod

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            htext = (base * (htext - ord(text[i]) * h) + ord(text[i + m])) % mod
            if htext < 0:
                htext += mod
    return -1


def kmp(text, pattern):
    n, m = len(text), len(pattern)

    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


sizes = [i * 10000 for i in range(1, 11)]

algorithms = {
    "Наивный": naive_search,
    "Бойер-Мур": boyer_moore,
    "Рабин-Карп": rabin_karp,
    "КМП": kmp
}

time_data = {name: [] for name in algorithms}

for size in sizes:
    text = "a" * (size - 1) + "b"
    pattern = "ab"

    print(f"\nДлина строки = {size}")

    for name, func in algorithms.items():
        elapsed, result = measure_time(func, text, pattern)
        time_data[name].append(elapsed)
        print(f"{name:12} | индекс = {result} | {elapsed:.6f} сек")

plot_results(
    x_values=sizes,
    times_dict=time_data,
    title="Сравнение алгоритмов поиска подстроки",
    x_label="Длина строки",
    y_label="Время выполнения (сек)"
)
