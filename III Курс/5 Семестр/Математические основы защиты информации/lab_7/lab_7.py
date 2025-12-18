def integer_sqrt(m):
    x = m
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + m // x) // 2
    return x

def binpow(a, d, p):
    result = 1
    base = a % p
    while d > 0:
        if d % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        d //= 2
    return result

def baby_step_giant_step(a, b, p):
    print("Метод 'шаг младенца – шаг великана'")
    print("Уравнение:", a, "^ x ≡", b, "(mod", p, ")")

    k = integer_sqrt(p) + 1
    print("k =", k)
    print()

    print("Последовательность y_n = a^(n*k) mod p")
    y_seq = []
    for n in range(1, k + 1):
        y = binpow(a, n * k, p)
        y_seq.append(y)
        if n <= 10:
            print("y_", n, "=", y, sep="")

    print()
    print("Последовательность z_n = b * a^n mod p")
    z_seq = []
    for n in range(0, k):
        z = (b * binpow(a, n, p)) % p
        z_seq.append(z)
        if n <= 10:
            print("z_", n, "=", z, sep="")
    print()

    print("Поиск совпадений между y_n и z_n")
    y_dict = {}
    for i, val in enumerate(y_seq, 1):
        y_dict[val] = i

    for j, val in enumerate(z_seq):
        if val in y_dict:
            i = y_dict[val]
            print("Найдено совпадение: y_", i, " = z_", j, " =", val, sep="")
            x = i * k - j
            print("x =", x)
            print()
            verification = binpow(a, x, p)
            print("Проверка:")
            print(a, "^", x, "mod", p, "=", verification)
            print()
            if verification == b:
                return x
            else:
                return None

    print("Совпадений не найдено")
    return None

def main():
    a = 15 # int(input("Введите a: "))
    b = 10870 # int(input("Введите b: "))
    p = 30323 # int(input("Введите p: "))

    print("Вычисление дискретного логарифма")
    print("a =", a, ", b =", b, ", p =", p)
    print()

    x = baby_step_giant_step(a, b, p)

    print("Результаты в формате отчета:")
    print("a =", a)
    print("b =", b)
    print("p =", p)
    print("x =", x)

main()
