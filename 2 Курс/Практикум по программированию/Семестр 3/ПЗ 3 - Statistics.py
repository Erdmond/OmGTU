import numpy as np
import scipy as sc
import statistics as stat


def print_mat(mat):
    p = np.array2string(mat, separator=', ',)
    p = p.replace('[', '').replace(']', '').replace(',', '').replace('. ', '.0')
    print(' ' + p)
    return


def print_stat(samp):
    print(f"""Среднее: {np.mean(samp)}
Мода: {stat.mode(samp) if len(np.unique(samp)) != len(samp) else "нет уникальной моды"}
Медиана: {np.median(samp)}
Минимум: {np.min(samp)}
Максимум: {np.max(samp)}
Стандартное отклонение: {np.std(samp)}
""")
    return


matrix = np.array([[3, -1.2, -8, 8], [21, -19, 0.5, 0], [7, 0, -4.9, -2], [1, -2, 13, 9]])
print("Исходная матрица:")
print_mat(matrix)
print()

P, L, U = sc.linalg.lu(matrix)
print("Нижняя треугольная матрица L:")
print_mat(L)
print()
print("Верхняя треугольная матрица U:")
print_mat(U)
print()
print("Матрица перестановок P:")
print_mat(P)
print()

det_mat = np.prod(np.diag(L)) * np.prod(np.diag(U)) * sc.linalg.det(np.linalg.inv(P))
print("Определитель матрицы: ", det_mat, sc.linalg.det(matrix))
print()

unif = np.random.uniform(low=-10, high=10, size=100)
norm = np.random.normal(loc=0, scale=20/3, size=100)
print("Равномерное распределение:")
print_mat(unif)
print()
print("Нормальное распределение:")
print_mat(norm)
print()

print("    Статистики для равномерного распределения:")
print_stat(unif)
print("    Статистики для нормального распределения:")
print_stat(norm)

print("Хи-квадрат тест для равномерного распределения:")
print(f"p-value: {sc.stats.chisquare(unif).pvalue}")
print("Хи-квадрат тест для нормального распределения:")
print(f"p-value: {sc.stats.chisquare(norm).pvalue}")
