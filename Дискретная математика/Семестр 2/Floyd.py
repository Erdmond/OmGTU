def floyd(graph):
    vertices_count = len(graph)
    for k in range(vertices_count):
        for i in range(vertices_count):
            for j in range(vertices_count):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

# Пример использования
points = int(input("Введите количество вершин графа: "))
print("Вводите весовую матрицу построчно через пробел: ")
graph = []
for i in range(points):
    graph.append(list(map(int, input().split())))
for i in range(points):
    for j in range(points):
        graph[i][j] = float('inf') if graph [i][j] == 0 else graph[i][j]
        if i == j:
            graph[i][j] = 0
print("Матрица кратчайших путей:")
print(floyd(graph))

# 0 10 18 8 0 0
# 10 0 16 9 21 0
# 0 16 0 0 0 15
# 7 9 0 0 0 12
# 0 0 0 0 0 23
# 0 0 15 0 23 0

# Ответ:
# Матрица кратчайших путей:
# [0, 10, 18, 8, 31, 20]
# [10, 0, 16, 9, 21, 21]
# [26, 16, 0, 25, 37, 15]
# [7, 9, 25, 0, 30, 12]
# [64, 54, 38, 63, 0, 23]
# [41, 31, 15, 40, 23, 0]
