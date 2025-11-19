def hash_code(item, seed:int=17) -> int:
    s = str(item)
    hash_val = 0
    for ch in s:
        hash_val = (hash_val * seed + ord(ch))
    return hash_val
