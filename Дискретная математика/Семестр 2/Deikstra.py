def min_distance(distances, visited):
    min_dist = float('inf')
    min_index = -1
    for v in range(len(distances)):
        if not visited[v] and distances[v] <= min_dist:
            min_dist = distances[v]
            min_index = v
    return min_index

def dijkstra(graph, start_vertex, end_vertex):
    vertices_count = len(graph)
    distances = [float('inf')] * vertices_count
    visited = [False] * vertices_count
    distances[start_vertex] = 0
    while not visited[end_vertex]:
        u = min_distance(distances, visited)
        visited[u] = True
        for v in range(vertices_count):
            if not visited[v] and graph[u][v] != 0 and distances[u] != float('inf') and distances[u] + graph[u][v] < distances[v]:
                distances[v] = distances[u] + graph[u][v]
    path = [end_vertex]
    temp_vertex = end_vertex
    while temp_vertex != start_vertex:
        for v in range(vertices_count):
            if graph[temp_vertex][v] != 0 and distances[temp_vertex] - graph[temp_vertex][v] == distances[v]:
                path.insert(0, v)
                temp_vertex = v
                break
    print(f"Кратчайший путь от вершины {start_vertex + 1} до вершины {end_vertex + 1}:")
    print(" -> ".join(str(vertex + 1) for vertex in path))
    print("Суммарное расстояние:", distances[end_vertex])

# Пример использования
points = int(input("Введите количество вершин графа: "))
print("Вводите весовую матрицу построчно через пробел: ")
graph = []
for i in range(points):
    graph.append(list(map(int, input().split())))
start_vertex = int(input("Введите стартовую вершину: ")) - 1
end_vertex = int(input("Введите конечную вершину: ")) - 1
dijkstra(graph, start_vertex, end_vertex)

# 6
# 0 5 0 0 2 4
# 5 0 12 0 0 1
# 0 12 0 9 0 3
# 0 0 9 0 7 10
# 2 0 0 7 0 8
# 4 1 3 10 8 0
# 1
# 4

# Ответ:
# Кратчайший путь от вершины 1 до вершины 4:
# 1 -> 5 -> 4
# Суммарное расстояние: 9