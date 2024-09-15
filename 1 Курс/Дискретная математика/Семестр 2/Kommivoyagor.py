def Kommivoyagor(graph):
    def bound():
        up_bound = 0
        for i in range(len(graph)):
            if i not in path:
                up_bound += min(graph[i])
        return up_bound
    def way(path, current_cost = 0):
        nonlocal min_cost, final_path
        if len(path) == len(graph):
            current_cost += graph[path[-1]][path[0]]
            if current_cost < min_cost:
                min_cost = current_cost
                final_path = [i + 1 for i in path]
            return
        for i in range(len(graph)):
            if i not in path:
                new_bound = bound_now + graph[path[-1]][i]
                if new_bound < min_cost:
                    new_path = path + [i]
                    way(new_path, current_cost + graph[path[-1]][i])
    min_cost = float('inf')
    final_path = []
    path = [0]
    bound_now = bound()
    way(path)
    return min_cost, final_path

graph = [
    [0, 41, 17, 23, 32],
    [13, 0, 45, 12, 37],
    [80, 45, 0, 50, 64],
    [23, 12, 50, 0, 67],
    [32, 37, 64, 67, 0]
]

cost, path = Kommivoyagor(graph)
print(f"Минимальная стоимость: {cost}")
print(f"Оптимальный путь: {path}")
