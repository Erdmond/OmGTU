def dfs_all_paths(graph, start=0, path=[]):
    path = path + [start]
    paths = [path]
    for node in range(len(graph[start])):
        if graph[start][node] == 1 and node not in path:
            new_paths = dfs_all_paths(graph, node, path)
            for new_path in new_paths:
                paths.append(new_path)
    out = []
    for i in paths:
        if len(i) == len(graph):
            out.append(i)
    return out

graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0]
]
all_paths_from_start = dfs_all_paths(graph)
cycles = []
ways = []
for i in all_paths_from_start:
    if (graph[i[-1]][i[0]] == 1) and (not(i in cycles)): cycles.append([o + 1 for o in i])
    elif not(i in ways): ways.append([o + 1 for o in i])
print(cycles)
print(ways)
