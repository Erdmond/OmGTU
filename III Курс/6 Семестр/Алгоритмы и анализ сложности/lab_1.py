from analisys.funcs import *

def fib_rec(n):
    if n < 3:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    k = 2
    num_1 = 1
    num_2 = 1
    if n < 3:
        return 1
    else:
        while k != n:
            num_1 = num_1 + num_2
            num_2 = num_1 - num_2
            k += 1
    return num_1


x = [i for i in range(1, 41)]

time_rec = []
time_iter = []

print(f'n: recursion | iterations')

for i in x:
    elapsed_rec, res_rec = measure_time(fib_rec, i)
    time_rec.append(elapsed_rec)

    elapsed_iter, res_iter = measure_time(fib_iter, i)
    time_iter.append(elapsed_iter)

    print(f'{i}: {res_rec} | {res_iter}')

time_dict = {
    'Рекурсивный': time_rec,
    'Итерационный': time_iter
}

plot_results(
    x_values=x,
    times_dict=time_dict,
    title="Сравнение алгоритмов вычисления чисел Фибоначчи",
    x_label="n (номер числа Фибоначчи)",
    y_label="Время выполнения (сек)"
)
