def floyd(graph):
    for i in range(points):
        for j in range(points):
            graph[i][j] = float('inf') if graph[i][j] == 0 else graph[i][j]
            if i == j:
                graph[i][j] = 0
    for k in range(points):
        for i in range(points):
            for j in range(points):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

def print_matrix(mat):
    for row in mat:
        for element in row:
            print(element, end="\t")
        print()

def short_way(start, end, graph):
    now = end - 1
    way = [str(end)]
    while now + 1 != start:
        min_point = ''
        min_ves = float('inf')
        for i in range(points):
            if graph[i][now] != 0 and graph[i][now] < min_ves:
                min_ves = graph[i][now]
                min_point = i
        way.append(str(min_point+1))
        now = min_point
    way.reverse()
    print(' -> '.join(way))
    return

# Пример использования
points = int(input("Введите количество вершин графа: "))
print("Вводите весовую матрицу построчно через пробел: ")
graph = []
for i in range(points):
    graph.append(list(map(int, input().split())))
print_matrix(graph)
print("Матрица кратчайших путей:")
graph_short = floyd(graph)
print_matrix(graph_short)
start = int(input("Введите точку от которой нужно найти путь: "))
end = int(input("Введите точку до которой нужно найти путь: "))
short_way(start, end, graph_short)
