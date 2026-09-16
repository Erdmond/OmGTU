from analisys.funcs import *
import random

def exhaustive_search(weights, costs, W):
    n = len(weights)
    max_cost = 0
    best_subset = []

    for mask in range(1 << n):
        total_weight = 0
        total_cost = 0
        subset = []

        for i in range(n):
            if mask & (1 << i):
                total_weight += weights[i]
                total_cost += costs[i]
                subset.append(i)

        if total_weight <= W and total_cost > max_cost:
            max_cost = total_cost
            best_subset = subset

    return best_subset, max_cost

def greedy_knapsack(weights, costs, W):
    items = list(range(len(weights)))
    items.sort(key=lambda i: costs[i] / weights[i], reverse=True)

    total_weight = 0
    total_cost = 0
    selected = []

    for i in items:
        if total_weight + weights[i] <= W:
            selected.append(i)
            total_weight += weights[i]
            total_cost += costs[i]

    return selected, total_cost

sizes = [5, 8, 10, 12, 14, 16, 18]
time_exhaustive = []
time_greedy = []

for n in sizes:
    weights = [random.randint(1, 15) for _ in range(n)]
    costs = [random.randint(1, 20) for _ in range(n)]
    W = sum(weights) // 2

    print(f"\nn = {n}")

    elapsed1, result1 = measure_time(exhaustive_search, weights, costs, W)
    subset1, cost1 = result1
    time_exhaustive.append(elapsed1)

    elapsed2, result2 = measure_time(greedy_knapsack, weights, costs, W)
    subset2, cost2 = result2
    time_greedy.append(elapsed2)

    print(f"Полный перебор | сумма = {cost1} | {elapsed1:.6f} сек")
    print(f"Жадный        | сумма = {cost2} | {elapsed2:.6f} сек")

    if cost2 > cost1:
        print("Ошибка: жадный дал результат лучше оптимального")

plot_results(
    x_values=sizes,
    times_dict={
        "Полный перебор": time_exhaustive,
        "Жадный алгоритм": time_greedy
    },
    title="Задача о рюкзаке: полный перебор vs жадный",
    x_label="Количество предметов",
    y_label="Время выполнения (сек)"
)
