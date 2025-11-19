from LAB_1.funcs.signature import *

class MinHash:
    def __init__(self, num_hashes=100):
        self.num_hashes = num_hashes

    def compute_similarity(self, set1, set2):
        assert len(set1) == len(set2), "The signature lengths must match"
        sig1 = compute_signature(set1, self.num_hashes)
        sig2 = compute_signature(set2, self.num_hashes)
        return sum(1 for i in range(len(sig1)) if sig1[i] == sig2[i]) / len(sig1)
