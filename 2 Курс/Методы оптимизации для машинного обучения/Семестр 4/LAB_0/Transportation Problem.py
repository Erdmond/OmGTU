import numpy as np
from collections import deque

def print_matrix(matrix):
    max_cols = len(matrix[0])
    col_widths = []
    for col in range(max_cols):
        max_width = max((len(str(row[col])) for row in matrix if col < len(row)))
        col_widths.append(max_width)
    for i, row in enumerate(matrix):
        row_str = " | ".join(str(item).rjust(col_widths[idx]) for idx, item in enumerate(row))
        if i == len(matrix) - 1 and len(row) < max_cols:
            row_str += " | " + "".rjust(col_widths[-1])
        print(f"{row_str}")
    print()

def min_in_matrix(matrix, skip_null=True):
    min_el = (matrix[0][0], 0, 0)
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) -1):
            if matrix[i][j] < min_el[0] and (matrix[i][j] != 0 or (not skip_null)):
                min_el = (matrix[i][j], i, j)
    return min_el

def max_in_matrix(matrix):
    max_el = (matrix[0][0], 0, 0)
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) -1):
            if matrix[i][j] > max_el[0]:
                max_el = (matrix[i][j], i, j)
    return max_el

def find_shortest_cycle(matrix, start):
    rows = len(matrix)
    cols = len(matrix[0])
    allowed = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] is not None:
                allowed.add((i, j))
    allowed.add(start)
    row_map = {}
    col_map = {}
    for i, j in allowed:
        row_map.setdefault(i, []).append((i, j))
        col_map.setdefault(j, []).append((i, j))
    queue = deque()
    queue.append((start, None, [start]))
    while queue:
        current, last_dir, path = queue.popleft()
        r, c = current
        candidates = set()
        if r in row_map:
            candidates.update(v for v in row_map[r] if v != current)
        if c in col_map:
            candidates.update(v for v in col_map[c] if v != current)
        for nb in candidates:
            dr, dc = nb[0] - r, nb[1] - c
            if dr != 0 and dc != 0:
                continue
            if dr != 0:
                new_dir = (1 if dr > 0 else -1, 0)
            else:
                new_dir = (0, 1 if dc > 0 else -1)
            if last_dir is not None:
                if last_dir[0] != 0 and new_dir[0] != 0:
                    continue
                if last_dir[1] != 0 and new_dir[1] != 0:
                    continue
            if nb == start:
                if len(path) >= 3:
                    return path
                else:
                    continue
            if nb in path:
                continue
            queue.append((nb, new_dir, path + [nb]))
    return None

class TransportationProblem:
    def __init__(self, price_matrix, count_matrix=None):
        self.price_matrix = price_matrix
        self.count_matrix = count_matrix

    def L(self):
        l = 0
        for i in range(len(self.price_matrix) - 1):
            for j in range(len(self.price_matrix[0]) - 1):
                if not (self.count_matrix[i][j] is None):
                    l += self.price_matrix[i][j] * self.count_matrix[i][j]
        return l

    def balance_check(self):
        sum_a = sum([self.price_matrix[i][-1] for i in range(len(self.price_matrix) - 1)])
        sum_b = sum(self.price_matrix[-1])
        if sum_a == sum_b: return True
        else: return False

    def closed_from_open(self):
        if self.balance_check():
            print('Задача уже имеет закрытый тип\n')
            return
        sum_a = sum([self.price_matrix[i][-1] for i in range(len(self.price_matrix) - 1)])
        sum_b = sum(self.price_matrix[-1])
        difference = sum_a - sum_b
        if difference > 0:
            for i in range(len(self.price_matrix) - 1):
                self.price_matrix[i].insert(-1, 0)
            self.price_matrix[-1].append(difference)
        else:
            difference = abs(difference)
            self.price_matrix.insert(-1, [0] * (len(self.price_matrix[0]) - 1))
            self.price_matrix[-2].append(difference)
        print_matrix(self.price_matrix)

    def northwest_corner(self):
        self.count_matrix = [[*i] for i in self.price_matrix]
        column_counter = 0
        for i in range(len(self.count_matrix) - 1):
            for j in range(len(self.count_matrix[0]) - 1):
                a_i = self.count_matrix[i][-1]
                b_j = self.count_matrix[-1][j]
                if a_i == 0:
                    self.count_matrix[i][j] = None
                    continue
                if j < column_counter:
                    self.count_matrix[i][j] = None
                    continue
                if b_j == 0:
                    self.count_matrix[i][j] = 0
                    continue
                minim = min(a_i, b_j)
                self.count_matrix[i][j] = minim
                self.count_matrix[i][-1] -= minim
                self.count_matrix[-1][j] -= minim
                column_counter = j
        self._fictive_price_calculation()
        print_matrix(self.count_matrix)

    def min_price(self):
        self.count_matrix = [[None] * (len(self.price_matrix[0]) - 1) + [self.price_matrix[i][-1]]
                             for i in range(len(self.price_matrix) - 1)]
        self.count_matrix.append([*self.price_matrix[-1]])
        new_price = [[*line] for line in self.price_matrix]
        max_price = max_in_matrix(self.price_matrix)[0] * 2
        while (sum([self.count_matrix[i][-1] for i in range(len(self.count_matrix[-1]))]) != 0
               and sum(self.count_matrix[-1]) != 0):
            min_price, i, j = min_in_matrix(new_price)
            if min_price == max_price: min_price, i, j = min_in_matrix(new_price, False)
            new_price[i][j] = max_price
            a_i = int(self.count_matrix[i][-1])
            b_j = int(self.count_matrix[-1][j])
            if a_i == 0 or b_j == 0: continue
            minim = min(a_i, b_j)
            self.count_matrix[i][-1] = a_i - minim
            self.count_matrix[-1][j] = b_j - minim
            self.count_matrix[i][j] = minim
        self._fictive_price_calculation()
        print_matrix(self.count_matrix)

    def _find_basis(self):
        basis = []
        for i in range(len(self.count_matrix) - 1):
            for j in range(len(self.count_matrix[0]) - 1):
                if not (self.count_matrix[i][j] is None):
                    basis.append((i, j))
        return basis

    def _fictive_price_calculation(self):
        basis = self._find_basis()
        mat_a = [[0 for _ in range(len(basis) + 1)] for _ in range(len(basis) + 1)]
        mat_y = [[0] for _ in range(len(basis) + 1)]
        mat_a[0][0] = 1
        for i in range(len(basis)):
            bas_i = basis[i][0]
            bas_j = basis[i][1]
            mat_a[i + 1][bas_i] = 1
            mat_a[i + 1][bas_j + len(self.price_matrix) - 1] = 1
            mat_y[i + 1] = [self.price_matrix[bas_i][bas_j]]
        prices = [int(el[0]) for el in np.linalg.inv(np.array(mat_a)) @ np.array(mat_y)]
        for i in range(len(self.count_matrix) - 1):
            for j in range(len(self.count_matrix[0]) - 1):
                self.count_matrix[i][-1] = prices[i]
                self.count_matrix[-1][j] = prices[i + j + 1]

    def _recalculation_cycle(self, points):
        max_diff, p_i, p_j = points[0]
        while points:
            point = points.pop()
            if point[0] > max_diff:
                max_diff, p_i, p_j = point
        matrix_of_ways = [[*line[:-1]] for line in self.count_matrix[:-1]]
        way = find_shortest_cycle(matrix_of_ways, (p_i, p_j))
        count_way = [(self.count_matrix[i][j], i, j) for i, j in way]
        min_diff = self.count_matrix[way[1][0]][way[1][1]]
        for i in range(len(count_way)):
            if (not (count_way[i][0] is None)
                and count_way[i][0] < min_diff and i % 2 == 1) : min_diff = count_way[i][0]
        one_null_flag = True
        for o in range(len(count_way)):
            count, i, j = count_way[o]
            if count is None:
                count = min_diff
            else: count = count + min_diff if o % 2 == 0 else count - min_diff
            if count == 0 and one_null_flag:
                self.count_matrix[i][j] = None
                one_null_flag = False
            else:
                self.count_matrix[i][j] = count

    def optim_check(self):
        non_optim_points = []
        for i in range(len(self.price_matrix) - 1):
            for j in range(len(self.price_matrix[0]) - 1):
                if (self.count_matrix[i][-1] + self.count_matrix[-1][j]) > self.price_matrix[i][j]:
                    non_optim_points.append(
                        (self.count_matrix[i][-1] + self.count_matrix[-1][j] - self.price_matrix[i][j], i, j))
        return non_optim_points

    def potential(self):
        while True:
            check = self.optim_check()
            if not check:
                break
            self._recalculation_cycle(check)

            self._fictive_price_calculation()
        print_matrix(self.count_matrix)
        print(f"L = {self.L()}")

str_mat = (
    '''40 36 9 20 24
26 11 22 26 42
6 3 12 3 23
5 37 33 26 36
35 29 21 35'''
)
mat = [list(map(int, x.split())) for x in str_mat.split('\n')]
task = TransportationProblem(mat)

print('Исходная задача:')
print_matrix(mat)

print('Определение типа:')
print('Закрытый тип\n') if task.balance_check() else print('Открытый тип\n')

print('Приведение к закрытому типу:')
task.closed_from_open()

print('Метод северо-западного угла:')
task.northwest_corner()
print('Значение целевой функции:')
print(f"{task.L()}\n")

print('Метод минимальной стоимости:')
task.min_price()
print('Значение целевой функции:')
print(f"{task.L()}\n")

print('Проверка оптимальности:')
print('Оптимальна\n') if not task.optim_check() else print('Неоптимальна\n')

print('Метод потенциалов:')
task.potential()
