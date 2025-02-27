import mmh3

def compute_signature(set_elements, num_hashes):
    signature = []
    for seed in range(num_hashes):
        min_hash = min(mmh3.hash(str(el), signed=False, seed=seed) % (2 ** 13 - 1) for el in set_elements)
        signature.append(min_hash)
    return signature
