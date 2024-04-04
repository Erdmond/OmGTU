def short_way(start, end, graph):
    if start == end:
        return 'петля'
    now = end
    way = [str(end)]
    while now != start:
        min_point = ''
        min_ves = float('inf')
        for i in range(points):
            if graph[i][now] != 0 and graph[i][now] < min_ves:
                min_ves = graph[i][now]
                min_point = i
        way.append(str(min_point+1))
        now = min_point
    way.reverse()
    return ' -> '.join(way)

def ford_bellman(graph, start):
    vertices_count = len(graph)
    distances = [float('inf')] * vertices_count
    distances[start] = 0
    ways = [[i for i in range(vertices_count)] for _ in range(vertices_count)]
    for o in range(vertices_count - 1):
        for u in range(vertices_count):
            for v in range(vertices_count):
                if graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]
                    ways[u][v] = u
    for u in range(vertices_count):
        for v in range(vertices_count):
            if graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]:
                print("Граф содержит отрицательный цикл")
                return
    return distances

points = int(input("Введите количество вершин графа: "))
print("Введите весовую матрицу построчно через пробел:")
graf = []
for i in range(points):
    graf.append(list(map(int, input().split())))
start = int(input("Введите стартовую вершину: ")) - 1
distances = ford_bellman(graf, start)
print("Кратчайшие расстояния и пути от вершины", start + 1, "до каждой вершины:")
for i in range(points):
    print(f"До вершины {i + 1}: {distances[i]}, путь: {short_way(start, i, graf)}")
