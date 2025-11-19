import mmh3

class CountMinSketch:
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.table = [[0] * width for _ in range(depth)]
        self.seeds = [17 + 2 * i for i in range(self.depth)]

    def add(self, item):
        for i in range(self.depth):
            index = mmh3.hash(item, signed=False, seed=i) % self.width
            self.table[i][index] += 1

    def estimate(self, item):
        return min(self.table[i][mmh3.hash(item, signed=False, seed=i) % self.width] for i in range(self.depth))
