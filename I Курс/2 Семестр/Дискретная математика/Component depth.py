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
def depth_func(point):
    if not point in gray_points:
        gray_points.append(point)
    if point in white_points:
        white_points.remove(point)
    for line in list(graf):
        if point in line:
            next_point = line[1] if point == line[0] else line[0]
            if next_point in white_points:
                graf.remove(line)
                depth_func(next_point)
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
while white_points:
    depth_func(white_points[0])
    component.append(gray_points)
    black_points += gray_points
    if white_points:
        gray_points = [white_points[0]]
print(component)
