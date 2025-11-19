def fill_matrix(data, count_picks):
    matrix = [[0] * count_picks for _ in range(count_picks)]
    for i in range(1, count_picks):
        peak, value = map(int, data[i].split())
        matrix[i][peak] = value
        matrix[peak][i] = value
        for j in range(i):
            if matrix[i][j] == 0:
                matrix[i][j] = value + matrix[peak][j]
                matrix[j][i] = value + matrix[peak][j]
    return matrix

def fill_berries(data, min_spel):
    berries = [int(line.split()[0]) for line in data if int(line.split()[1]) >= min_spel]
    return berries

def find_min_way(matrix, location, way):
    min_ways = [matrix[location][w] for w in way]
    min_value = min(min_ways)
    index = min_ways.index(min_value)
    return min_value, way[index]

def give_answer(matrix, location, berries):
    total_sum = 0
    while berries:
        min_way, location = find_min_way(matrix, location, berries)
        total_sum += min_way
        berries.remove(location)
    return total_sum

for i in range(1, 26):
    u = f'0{i}' if i < 10 else f'{i}'
    with open(f"OLYMP/- Eat/input_s1_{u}.txt", 'r') as file:
        data = file.readlines()
    first_line = data[0].split()
    count_peaks = int(first_line[0]) + 1
    count_berries = int(first_line[1])
    matrix = fill_matrix(data, count_peaks)
    last_line = list(map(int, data[-1].split()))
    location = last_line[0]
    min_spel = last_line[1]
    data_copy = data[count_peaks:count_peaks + count_berries]
    berries = fill_berries(data_copy, min_spel)
    my_answer = give_answer(matrix, location, berries)
    with open(f"OLYMP/- Eat/output_s1_{u}.txt", 'r') as file:
        real_answer = int(file.read().strip())
    if my_answer == real_answer:
        print(f"{i}: True")
    else:
        print(f"{i}: {my_answer} {real_answer}")

"""
Ошибочные тесты: 2, 22, 23, 24, 25
"""