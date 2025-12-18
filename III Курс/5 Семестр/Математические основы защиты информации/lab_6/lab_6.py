def integer_sqrt(m):
    x = m
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + m // x) // 2
    return x

def is_perfect_square(n):
    if n < 0:
        return False
    r = integer_sqrt(n)
    return r * r == n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def quadratic_residue(a, p):
    if a % p == 0:
        return True
    for x in range(p):
        if (x * x) % p == a % p:
            return True
    return False

def quadratic_sieve(m, a, b, c):
    print("Метод квадратичного решета")
    print("m =", m)
    print("a =", a, ", b =", b, ", c =", c)
    sieve_a = []
    for x in range(a):
        x2 = (x * x) % a
        z = (x2 - m) % a
        sieve_a.append((x, x2, z, quadratic_residue(z, a)))
    sieve_b = []
    for x in range(b):
        x2 = (x * x) % b
        z = (x2 - m) % b
        sieve_b.append((x, x2, z, quadratic_residue(z, b)))
    sieve_c = []
    for x in range(c):
        x2 = (x * x) % c
        z = (x2 - m) % c
        sieve_c.append((x, x2, z, quadratic_residue(z, c)))
    print("Таблица по модулю a:")
    for i, row in enumerate(sieve_a):
        print(i, row)
    print("Таблица по модулю b:")
    for i, row in enumerate(sieve_b):
        print(i, row)
    print("Таблица по модулю c:")
    for i, row in enumerate(sieve_c):
        print(i, row)
    start = integer_sqrt(m) + 1
    end = (m + 1) // 2
    print("Интервал:", start, "-", end)
    for x in range(start, end + 1):
        z = x * x - m
        if quadratic_residue(z % a, a) and quadratic_residue(z % b, b) and quadratic_residue(z % c, c):
            print("Подходящее x:", x, "Z =", z)
            if is_perfect_square(z):
                y = integer_sqrt(z)
                print("Найден y:", y)
                p = x + y
                q = x - y
                print("p =", p, ", q =", q)
                return x, y, p, q
    print("Не найдено подходящих значений")
    return None, None, None, None

def rho_method(m, x0):
    print("ρ-метод факторизации")
    print("n =", m)
    def f(x):
        return (x * x + 1) % m
    x1 = x0
    x2 = x0
    for step in range(1, 501):
        x1 = f(x1)
        x2 = f(f(x2))
        a_n = abs(x1 - x2)
        d_n = gcd(a_n, m)
        print("Шаг", step, "x1 =", x1, "x2 =", x2, "a_n =", a_n, "d_n =", d_n)
        if 1 < d_n < m:
            p = d_n
            q = m // d_n
            print("Найден делитель на шаге", step)
            print("p =", p, ", q =", q)
            return step, a_n, d_n, p, q
    print("Не найден делитель")
    return None, None, None, None, None

def main():
    m = 540737
    # m = int(input("Введите m: "))
    # a = 3
    # b = 5
    # c = 7
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    x, y, p1, q1 = quadratic_sieve(m, a, b, c)
    print()
    # x0 = 2
    x0 = int(input("Введите x0: "))
    step, a_n, d_n, p2, q2 = rho_method(m, x0)
    print()
    print("Результаты в формате отчета:")
    print("m =", m)
    print("a =", a, ", b =", b, ", c =", c)
    print("x =", x, ", y =", y)
    print("p =", p1, ", q =", q1)
    print()
    print("n =", m)
    print("a_n =", a_n, ", d_n =", d_n)
    print("p =", p2, ", q =", q2)

main()
