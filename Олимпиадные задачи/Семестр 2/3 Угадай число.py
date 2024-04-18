def fokus(num, strk, x):
    v, n = strk.split()
    if n == "x": n = x
    if v == "+": return num + int(n)
    if v == "-": return num - int(n)
    if v == "*": return num * int(n)
    if v == "/": return num / int(n)

s = open("OLYMP/Num/input_s1_01.txt").readlines()
for x in range(-100, 101):
    t = x
    for i in range(1, len(s) - 1):
        t = fokus(t, s[i], x)
    if t == int(s[len(s) - 1]):
        print(x)
        break
