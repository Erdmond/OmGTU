from LAB_1.funcs.hash import *

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
        self.seeds = [17 + 2 * i for i in range(self.hash_count)]

    def _hashes(self, item):
        positions = []
        for seed in self.seeds:
            positions.append(hash_code(item, seed) % self.size)
        return positions

    def add(self, item):
        for pos in self._hashes(item):
            self.bit_array[pos] = 1

    def __contains__(self, item):
        return all(self.bit_array[pos] for pos in self._hashes(item))

    def __or__(self, other):
        if self.size != other.size or self.hash_count != other.hash_count:
            raise ValueError("The filter characteristics must match")
        new_filter = BloomFilter(self.size, self.hash_count)
        new_filter.bit_array = [max(a, b) for a, b in zip(self.bit_array, other.bit_array)]
        return new_filter

    def __and__(self, other):
        if self.size != other.size or self.hash_count != other.hash_count:
            raise ValueError("The filter characteristics must match")
        new_filter = BloomFilter(self.size, self.hash_count)
        new_filter.bit_array = [min(a, b) for a, b in zip(self.bit_array, other.bit_array)]
        return new_filter
