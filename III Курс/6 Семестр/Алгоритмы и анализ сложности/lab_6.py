from analisys.funcs import *
import random

def max_non_overlapping(segments):
    segments = sorted(segments, key=lambda x: x[1])
    result = []
    last_end = -float('inf')
    for l, r in segments:
        if l >= last_end:
            result.append((l, r))
            last_end = r
    return result

def max_requests(requests):
    requests = sorted(requests, key=lambda x: x[1])
    result = []
    last_end = -float('inf')
    for start, end in requests:
        if start >= last_end:
            result.append((start, end))
            last_end = end
    return result

def min_cover(segments, L, R):
    segments = sorted(segments, key=lambda x: x[0])
    result = []
    i = 0
    n = len(segments)
    current = L
    while current < R:
        best = None
        while i < n and segments[i][0] <= current:
            if best is None or segments[i][1] > best[1]:
                best = segments[i]
            i += 1
        if best is None:
            return []
        result.append(best)
        current = best[1]
    return result

def generate_covering_segments(n, L, R):
    segments = []
    k = max(10, n // 50)
    base_len = (R - L) / k
    overlap = base_len * 0.25
    for i in range(k):
        start = L + i * base_len - overlap
        end = L + (i + 1) * base_len + overlap
        start = max(L, start)
        end = min(R, end)
        segments.append((start, end))
    while len(segments) < n:
        a = random.uniform(L, R)
        b = random.uniform(L, R)
        l, r = min(a, b), max(a, b)
        if l <= L and r >= R:
            continue
        segments.append((l, r))
    random.shuffle(segments)
    return segments


sizes = [i * 1000 for i in range(1, 11)]

print("\nЗадание 1.")
time_task1 = []
for size in sizes:
    segments = [(random.randint(0, size), random.randint(0, size)) for _ in range(size)]
    segments = [(min(l, r), max(l, r)) for l, r in segments]
    elapsed, result = measure_time(max_non_overlapping, segments)
    time_task1.append(elapsed)
    print(f"n = {size} | выбрано = {len(result)} | {elapsed:.6f} сек")

plot_results(
    x_values=sizes,
    times_dict={"Макс. непересекающиеся": time_task1},
    title="Жадный выбор непересекающихся отрезков",
    x_label="Количество отрезков",
    y_label="Время выполнения (сек)"
)

print("\nЗадание 2.")
time_task2 = []
for size in sizes:
    requests = [(random.randint(0, size), random.randint(0, size)) for _ in range(size)]
    requests = [(min(s, e), max(s, e)) for s, e in requests]
    elapsed, result = measure_time(max_requests, requests)
    time_task2.append(elapsed)
    print(f"n = {size} | принято заявок = {len(result)} | {elapsed:.6f} сек")

plot_results(
    x_values=sizes,
    times_dict={"Макс. заявки": time_task2},
    title="Жадный выбор заявок",
    x_label="Количество заявок",
    y_label="Время выполнения (сек)"
)


print("\nЗадание 3.")
time_task3 = []
for size in sizes:
    L = 0.0
    R = float(size)
    segments = generate_covering_segments(size, L, R)
    elapsed, result = measure_time(min_cover, segments, L, R)
    time_task3.append(elapsed)
    ok = "OK" if result and result[-1][1] >= R else "FAILED"
    print(f"n = {size} | использовано отрезков = {len(result)} | {elapsed:.6f} сек | {ok}")

plot_results(
    x_values=sizes,
    times_dict={"Минимальное покрытие": time_task3},
    title="Жадное покрытие интервала",
    x_label="Количество отрезков",
    y_label="Время выполнения (сек)"
)
