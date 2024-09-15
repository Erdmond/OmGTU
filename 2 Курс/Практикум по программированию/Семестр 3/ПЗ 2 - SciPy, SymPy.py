import math
import scipy
import sympy
import numpy as np


def f_1(ks):
    return math.sin(math.sqrt(2 * ks))


x_o = 3.5
first_derivative = scipy.misc.derivative(f_1, x_o, dx=1e-6)
second_derivative = scipy.misc.derivative(f_1, x_o, dx=1e-6, n=2)
print(f"Первая производная в точке {x_o}: {first_derivative}")
print(f"Вторая производная в точке {x_o}: {second_derivative}")

x = sympy.symbols('x')
funk = sympy.sin(sympy.sqrt(2 * x))
first_derivative = sympy.diff(funk, x)
second_derivative = sympy.diff(funk, x, 2)
print(f"Первая производная: {sympy.simplify(first_derivative)}")
print(f"Вторая производная: {sympy.simplify(second_derivative)}")

integral = scipy.integrate.quad(f_1, 0, 1)
print(f"Интеграл: {integral[0]}")

n_integral = sympy.integrate(funk, x)
print(f"Неопределённый интеграл: {n_integral}")


def f_2(ks):
    return (ks[0] + 3) ** 3 + (ks[1] - 3) ** 2


result = scipy.optimize.minimize(f_2, np.ones(2), constraints=[
    scipy.optimize.LinearConstraint([1, -4], [12], [np.inf]),
    scipy.optimize.LinearConstraint([[1, 0], [0, 1]], [0, 0], [np.inf, np.inf])])
print(result)
