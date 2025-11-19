a = int(input("Введите количество строк: "))
b = int(input("Введите количество столбцов: "))
pole = [['' for x in range(b)] for y in range(a)]
print("Вводите внутренние стенки в формате строка-столбец, введите x чтобы завершить:")
s = ''
while True:
    s = input().split()
    if s[0] == 'x':
        break
    s = list(map(int, s))
    pole[s[0]][s[1]] = 'x'
print("Введите стартовую позицию: ", end='')
start = [int(input()) - 1, int(input()) - 1]
pole[start[0]][start[1]] = 0
print("Введите финальную позицию: ", end='')
end = [int(input()) - 1, int(input()) - 1]
k = 0
while pole[end[0]][end[1]] == '':
    pre_pole = list(pole)
    for i in range(a):
        for j in range(b):
            if pole[i][j] == k:
                if 0 <= i - 1 < a and pole[i - 1][j] != 'x':
                    pole[i - 1][j] = k + 1 if pole[i - 1][j] == '' else min(k + 1, int(pole[i - 1][j]))
                if 0 <= i + 1 < a and pole[i + 1][j] != 'x':
                    pole[i + 1][j] = k + 1 if pole[i + 1][j] == '' else min(k + 1, int(pole[i + 1][j]))
                if 0 <= j - 1 < b and pole[i][j - 1] != 'x':
                    pole[i][j - 1] = k + 1 if pole[i][j - 1] == '' else min(k + 1, int(pole[i][j - 1]))
                if 0 <= j + 1 < b and pole[i][j + 1] != 'x':
                    pole[i][j + 1] = k + 1 if pole[i][j + 1] == '' else min(k + 1, int(pole[i][j + 1]))
                if 0 <= i - 1 < a and 0 <= j - 1 < b and pole[i - 1][j - 1] != 'x':
                    pole[i - 1][j - 1] = k + 1 if pole[i - 1][j - 1] == '' else min(k + 1, int(pole[i - 1][j - 1]))
                if 0 <= i - 1 < a and 0 <= j + 1 < b and pole[i - 1][j + 1] != 'x':
                    pole[i - 1][j + 1] = k + 1 if pole[i - 1][j + 1] == '' else min(k + 1, int(pole[i - 1][j + 1]))
                if 0 <= i + 1 < a and 0 <= j - 1 < b and pole[i + 1][j - 1] != 'x':
                    pole[i + 1][j - 1] = k + 1 if pole[i + 1][j - 1] == '' else min(k + 1, int(pole[i + 1][j - 1]))
                if 0 <= i + 1 < a and 0 <= j + 1 < b and pole[i + 1][j + 1] != 'x':
                    pole[i + 1][j + 1] = k + 1 if pole[i + 1][j + 1] == '' else min(k + 1, int(pole[i + 1][j + 1]))
    k += 1
    if pole == pre_pole:
        print("Финальная точка недостижима.")
        break
# Обратный путь
way = [0]
now = list(end)
while way[-1] != [3, 0]:
    hods = []
    i = now[0]
    j = now[1]
    if 0 <= i - 1 < a and pole[i - 1][j] != 'x':
        hods.append([i - 1, j, pole[i - 1][j]])
    if 0 <= i + 1 < a and pole[i + 1][j] != 'x':
        hods.append([i + 1, j, pole[i + 1][j]])
    if 0 <= j - 1 < b and pole[i][j - 1] != 'x':
        hods.append([i, j - 1, pole[i][j - 1]])
    if 0 <= j + 1 < b and pole[i][j + 1] != 'x':
        hods.append([i, j + 1, pole[i][j + 1]])
    if 0 <= i - 1 < a and 0 <= j - 1 < b and pole[i - 1][j - 1] != 'x':
        hods.append([i - 1, j - 1, pole[i - 1][j - 1]])
    if 0 <= i - 1 < a and 0 <= j + 1 < b and pole[i - 1][j + 1] != 'x':
        hods.append([i - 1, j + 1, pole[i - 1][j + 1]])
    if 0 <= i + 1 < a and 0 <= j - 1 < b and pole[i + 1][j - 1] != 'x':
        hods.append([i + 1, j - 1, pole[i + 1][j - 1]])
    if 0 <= i + 1 < a and 0 <= j + 1 < b and pole[i + 1][j + 1] != 'x':
        hods.append([i + 1, j + 1, pole[i + 1][j + 1]])
    hods = sorted(hods, key=lambda x: x[2])
    now = [hods[0][0], hods[0][1]]
    way.append([hods[0][0], hods[0][1]])
way.remove(0)
way = list(reversed(way))
print(way)
print(k)
