import math
import mmh3
from LAB_1.funcs.alpha import *

class HyperLogLog:
    def __init__(self, precision: int = 14):
        if not (4 <= precision <= 16):
            raise ValueError("Precision should be in range [4, 16]")
        self.p = precision
        self.m = 1 << precision
        self.alpha_m = get_alpha(self.m)
        self.registers = [0] * self.m

    def add(self, value):
        hash_value = mmh3.hash(str(value), signed=False)
        index = hash_value & (self.m - 1)
        w = hash_value >> self.p
        max_bits = 32 - self.p
        if w == 0:
            leading_zeros = max_bits + 1
        else:
            leading_zeros = max_bits - w.bit_length() + 1
        self.registers[index] = max(self.registers[index], leading_zeros)

    def estimate(self) -> int:
        sum_registers = sum(2.0 ** -r for r in self.registers)
        raw_estimate = self.alpha_m * self.m ** 2 / sum_registers
        if raw_estimate <= 2.5 * self.m:
            zeros = self.registers.count(0)
            if zeros > 0:
                raw_estimate = self.m * math.log(self.m / zeros)
        return int(raw_estimate)
