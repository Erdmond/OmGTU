# Компонента связности в ширину (Ответ: [1,2,3,4,5,6,7,8],[9,10,11])
"""
12
1 4
1 2
4 5
2 5
2 3
3 5
5 6
6 7
6 8
9 10
10 11
11 9
"""
lines = int(input())
graf = []
for i in range(lines):
    graf.append(str(input()).split())
white_points = []
for i in graf:
    if not (i[0] in white_points): white_points.append(i[0])
    if not (i[1] in white_points): white_points.append(i[1])
component = []
black_points = []
gray_points = [white_points[0]]
white_points.remove(white_points[0])
while True:
    del_ways = []
    if len(gray_points) != 0:
        for p in graf:
            if (p[0] == gray_points[0]) and (not (p[1] in gray_points)) and (p[1] in white_points):
                gray_points.append(p[1])
                white_points.remove(p[1])
                del_ways.append(p)
            elif (p[1] == gray_points[0]) and (not (p[0] in gray_points)) and (p[1] in white_points):
                gray_points.append(p[0])
                white_points.remove(p[0])
                del_ways.append(p)
            elif not (p[0] in white_points) and (not (p[1] in white_points)):
                del_ways.append(p)
        for w in del_ways:
            graf.remove(w)
        black_points.append(gray_points[0])
        gray_points.remove(gray_points[0])
    else:
        component.append(black_points)
        black_points = []
        gray_points = [white_points[0]]
    if len(graf) == 0:
        component.append(black_points + gray_points)
        break
print(component)
