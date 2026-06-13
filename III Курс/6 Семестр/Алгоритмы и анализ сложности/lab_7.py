from analisys.funcs import *
import random

def maximize_tasks_sum(tasks):
    tasks_sorted = sorted(tasks, key=lambda x: x["cost"], reverse=True)

    max_deadline = max(task["deadline"] for task in tasks_sorted)
    schedule = [None] * (max_deadline + 1)
    total_cost = 0

    for task in tasks_sorted:
        for day in range(task["deadline"], 0, -1):
            if schedule[day] is None:
                schedule[day] = task["id"]
                total_cost += task["cost"]
                break

    return schedule[1:], total_cost

def children_matinee(ages):
    ages_sorted = sorted(ages)

    groups = 1
    min_age = ages_sorted[0]

    for age in ages_sorted[1:]:
        if age - min_age > 2:
            groups += 1
            min_age = age

    return groups


print("\nЗадание 1.")

sizes = [i * 1000 for i in range(1, 11)]
time_task1 = []

for size in sizes:
    tasks = []
    for i in range(size):
        tasks.append({
            "id": i,
            "deadline": random.randint(1, size // 10 + 1),
            "cost": random.randint(1, 1000)
        })

    elapsed, result = measure_time(maximize_tasks_sum, tasks)
    schedule, total = result
    time_task1.append(elapsed)

    print(f"n = {size} | выполнено = {len([x for x in schedule if x is not None])} | сумма = {total} | {elapsed:.6f} сек")

plot_results(
    x_values=sizes,
    times_dict={"Макс. сумма заказов": time_task1},
    title="Жадное планирование заказов",
    x_label="Количество заказов",
    y_label="Время выполнения (сек)"
)


print("\nЗадание 2.")

sizes = [i * 1000 for i in range(1, 11)]
time_task2 = []

for size in sizes:
    ages = [random.randint(0, 20) for _ in range(size)]

    elapsed, groups = measure_time(children_matinee, ages)
    time_task2.append(elapsed)

    print(f"n = {size} | групп = {groups} | {elapsed:.6f} сек")

plot_results(
    x_values=sizes,
    times_dict={"Минимум групп": time_task2},
    title="Группировка детей по возрасту",
    x_label="Количество детей",
    y_label="Время выполнения (сек)"
)
