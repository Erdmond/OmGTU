def Day_In_Month(x, y):
    if (x == 1) or (x == 3) or (x == 5) or (x == 7) or (x == 8) or (x == 10) or (x == 12):
        return 31
    if (x == 4) or (x == 6) or (x == 9) or (x == 11):
        return 30
    if (x == 2) and (y % 4 == 0):
        return 29
    if (x == 2) and (y % 4 != 0):
        return 28


f = open('OLYMP/Интенсификация производства/input_s1_01.txt')
s = [str(i) for i in f]

Date_1 = s[0].split('.')
Date_2 = s[1].split('.')

D1 = int(Date_1[0])
M1 = int(Date_1[1])
Y1 = int(Date_1[2])
D2 = int(Date_2[0])
M2 = int(Date_2[1])
Y2 = int(Date_2[2])

Product_Now = int(s[2])

Days1 = 0
for x in range(0, Y2 + 1):
    if x % 4 == 0:
        Days1 += 366
    else:
        Days1 += 365
for x in range(1, M2):
    Days1 += Day_In_Month(x, Y2)
Days1 += D2

Days2 = 0
for x in range(0, Y1 + 1):
    if x % 4 == 0:
        Days2 += 366
    else:
        Days2 += 365
for x in range(1, M1):
    Days2 += Day_In_Month(x, Y1)
Days2 += D1
Days = Days1 - Days2 + 1

Product = ((2 * Product_Now + (Days - 1)) / 2) * Days

f = open('OLYMP/Интенсификация производства/output_s1_01.txt')
s = [int(i) for i in f]

if Product == s[0]:
    print('Верно')
else:
    print('Неверно, должно быть ' + str(s[0]) + ', а у меня ' + str(Product))

# Не работают тесты: 5, 3;
# Остальные работают.
