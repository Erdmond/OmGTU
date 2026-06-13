from analisys.funcs import *
import random

def build_conflict_graph(matrix):
    n = len(matrix)
    adj = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            conflict = False
            for k in range(len(matrix[0])):
                if matrix[i][k] == 1 and matrix[j][k] == 1:
                    conflict = True
                    break
            if conflict:
                adj[i][j] = 1
                adj[j][i] = 1
    return adj

def greedy_coloring(matrix):
    n = len(matrix)
    adj = build_conflict_graph(matrix)

    colors = [0] * n

    for v in range(n):
        used = set()
        for u in range(n):
            if adj[v][u] == 1 and colors[u] != 0:
                used.add(colors[u])

        color = 1
        while color in used:
            color += 1
        colors[v] = color

    schedule = {}
    for i in range(n):
        schedule.setdefault(colors[i], []).append(i)

    return schedule, max(colors)

def greedy_bin_packing(items, capacity):
    containers = []

    for item in items:
        placed = False
        for container in containers:
            if sum(container) + item <= capacity:
                container.append(item)
                placed = True
                break
        if not placed:
            containers.append([item])

    return containers


print("\nЗадание 1.")

example_matrix = [
    [1,0,0,1,0,1,0,0,0,1],
    [0,1,1,0,0,0,1,0,1,0],
    [0,1,0,0,1,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,1,0],
    [1,0,0,0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0,1,0,1],
    [0,0,1,1,0,1,0,0,0,0],
    [1,0,0,0,0,0,0,1,0,0],
    [0,0,1,1,0,1,1,0,0,1]
]

elapsed, result = measure_time(greedy_coloring, example_matrix)
schedule, min_time = result

print("Расписание:", schedule)
print("Минимальное время:", min_time)
print("Время работы:", f"{elapsed:.6f} сек")

sizes = [10, 20, 30, 40, 50]
time_task1 = []

for n in sizes:
    m = n
    matrix = [[random.randint(0,1) for _ in range(m)] for _ in range(n)]
    elapsed, _ = measure_time(greedy_coloring, matrix)
    time_task1.append(elapsed)

plot_results(
    x_values=sizes,
    times_dict={"Раскраска графа": time_task1},
    title="Жадная раскраска графа",
    x_label="Количество работ",
    y_label="Время выполнения (сек)"
)

print("\nЗадание 2.")

sizes = [100, 200, 300, 400, 500]
time_task2 = []

for n in sizes:
    items = [round(random.uniform(0.1, 0.7), 2) for _ in range(n)]
    capacity = 1.0

    elapsed, containers = measure_time(greedy_bin_packing, items, capacity)
    time_task2.append(elapsed)

    print(f"n = {n} | контейнеров = {len(containers)} | {elapsed:.6f} сек")

plot_results(
    x_values=sizes,
    times_dict={"First-Fit": time_task2},
    title="Жадное размещение грузов",
    x_label="Количество грузов",
    y_label="Время выполнения (сек)"
)
