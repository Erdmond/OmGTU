from analisys.funcs import *
import random

random.seed(0)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if i == 0 or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


sizes = [i * 100 for i in range(1, 11)]
sort_functions = {
    'Пузырёк': bubble_sort,
    'Гномья': gnome_sort,
    'Вставками': insertion_sort
}

print("Случайные данные:")
time_random = {name: [] for name in sort_functions}

for size in sizes:
    arr_random = [random.randint(1, 10000) for _ in range(size)]
    
    for name, func in sort_functions.items():
        elapsed, _ = measure_time(func, arr_random.copy())
        time_random[name].append(elapsed)
    
    print(f"{size} | ", end="")
    for name in sort_functions:
        print(f"{time_random[name][-1]:.4f} ", end="")
    print()

plot_results(
    x_values=sizes,
    times_dict=time_random,
    title="Сортировка случайных данных",
    x_label="Размер массива",
    y_label="Время выполнения (сек)"
)


print("\nОтсортированные данные:")
time_sorted = {name: [] for name in sort_functions}

for size in sizes:
    arr_sorted = sorted([random.randint(1, 10000) for _ in range(size)])
    
    for name, func in sort_functions.items():
        elapsed, _ = measure_time(func, arr_sorted.copy())
        time_sorted[name].append(elapsed)
    
    print(f"{size} | ", end="")
    for name in sort_functions:
        print(f"{time_sorted[name][-1]:.4f} ", end="")
    print()

plot_results(
    x_values=sizes,
    times_dict=time_sorted,
    title="Сортировка уже отсортированных данных",
    x_label="Размер массива",
    y_label="Время выполнения (сек)"
)
