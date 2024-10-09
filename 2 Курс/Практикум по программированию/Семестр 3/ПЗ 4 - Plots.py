import math
import numpy as np
import matplotlib.pyplot as plt


def f_1(ks):
    return math.sin(math.sqrt(2 * ks))


def f_2(a, b):
    return (a + 3)**3 + (b - 3)**2


x = np.linspace(0, 1, 101)
y = [f_1(i) for i in x]
print(x)
print(y)

plt.plot(x, y, label='sin(sqrt(2*x))')
plt.title('График', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14, rotation=0)
plt.legend(fontsize=12)
plt.show()

plt.plot(x, y, 'ko', color="#ff6961", markersize=2, label='sin(sqrt(2*x))')
plt.title('Точечный график функции', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14, rotation=0)
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.5, alpha=0.5)
plt.legend(fontsize=12)
plt.show()

unif = np.random.uniform(low=-10, high=10, size=100)
norm = np.random.normal(loc=0, scale=20/3, size=100)
plt.hist(unif, bins=100, color='skyblue', label='Равномерное распределение')
plt.hist(norm, bins=100, color='salmon', label='Нормальное распределение')
plt.title('Гистограммы', fontsize=16)
plt.xlabel('Значения', fontsize=14)
plt.ylabel('Частота', fontsize=14)
plt.legend(fontsize=12)
plt.show()

sample = np.random.randint(1, 5, size=50)
nums, counts = np.unique(sample, return_counts=True)
plt.pie(counts, labels=nums, startangle=90, colors=['#ff6961', '#ff9933', '#ffe599', '#90ee90'])
plt.title('Круговая диаграмма')
plt.show()
plt.bar(nums, counts, color=['#ff6961', '#ff9933', '#ffe599', '#90ee90'])
plt.xlabel('Числа')
plt.ylabel('Частота')
plt.title('Столбчатая диаграмма')
plt.xticks(nums)
plt.show()

x1 = np.linspace(-5, 5, 50)
x2 = np.linspace(-5, 5, 50)
X1, X2 = np.meshgrid(x1, x2)
Z = f_2(X1, X2)
graph = plt.figure().add_subplot(111, projection='3d')
graph.plot_surface(X1, X2, Z, color='lightgreen')
graph.set_xlabel('X1')
graph.set_ylabel('X2')
graph.set_zlabel('Z')
plt.show()


def show_graph_grid(style):
    plt.style.use(style)
    fig = plt.figure()
    fig.suptitle('Сетка графиков', fontsize=16)
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x, y, label='sin(sqrt(2*x))')
    ax1.set_title('График')
    ax1.set_xlabel('x', fontsize=14)
    ax1.set_ylabel('y', fontsize=14, rotation=0)
    ax1.legend()
    ax1.set_facecolor('#f2f2f2')
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(x, y, 'ko', markersize=2, label='sin(sqrt(2*x))')
    ax2.set_title('Точечный график')
    ax2.set_xlabel('x', fontsize=14)
    ax2.set_ylabel('y', fontsize=14, rotation=0)
    ax2.grid(True, color='lightgray', linestyle='-', linewidth=0.5, alpha=0.5)
    ax2.legend()
    ax2.set_facecolor('#f2f2f2')
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.pie(counts, labels=nums, autopct='%1.1f%%', startangle=90,
            colors=['#ff6961', '#ff9933', '#ffe599', '#90ee90', '#99ccff'])
    ax3.set_title('Круговая диаграмма')
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    ax4.plot_surface(X1, X2, Z, color='lightgreen')
    ax4.set_xlabel('X1')
    ax4.set_ylabel('X2')
    ax4.set_zlabel('Z')
    ax4.set_title('Трехмерный график')
    plt.show()


show_graph_grid('default')
show_graph_grid('classic')
show_graph_grid('Solarize_Light2')
show_graph_grid('dark_background')
