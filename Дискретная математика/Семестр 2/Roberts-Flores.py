def next_vertex(graph, path, pos, v):
    if graph[path[pos-1]][v] == 0:
        return False
    for vertex in path:
        if vertex == v:
            return False
    return True

def hamilton_path(graph, path, pos):
    n = len(graph)
    if pos == n:
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, n):
        if next_vertex(graph, path, pos, v):
            path[pos] = v
            if hamilton_path(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0]
]
path = [-1] * len(graph)
path[0] = 0
hamilton_way = hamilton_path(graph, path, 1)
if not hamilton_way:
    print("Гамильтонов путь не найден")
else:
    print([i + 1 for i in path])
