def to_star(parts):
    return ' + '.join(f"{k}*{p}" for k, p in parts)

def expanded(parts):
    terms = []
    for k, p in parts:
        terms.extend([str(p)] * k)
    return '+'.join(terms)

def normalize(parts):
    if not parts:
        return []
    parts.sort(key=lambda x: -x[1])
    res = []
    cur_k, cur_p = parts[0]
    for k, p in parts[1:]:
        if p == cur_p:
            cur_k += k
        else:
            res.append([cur_k, cur_p])
            cur_k, cur_p = k, p
    res.append([cur_k, cur_p])
    return res

def next_step(partition):
    m = len(partition)
    km, pm = partition[-1]

    if km > 1:
        if pm == 1:
            rem = km - 2
            exclude = f"2*{pm}"
            add = f"1*{pm+1}"
            remainder = f"{rem}*1" if rem > 0 else "0"
            new_parts = partition[:-1]
            if rem > 0:
                new_parts.append([rem, 1])
            new_parts.append([1, pm+1])
        else:
            rem = pm - 1
            exclude = f"2*{pm}"
            add = f"1*{pm+1}"
            remainder = f"{rem}*1" if rem > 0 else "0"
            new_parts = partition[:-1]
            if km - 2 > 0:
                new_parts.append([km - 2, pm])
            new_parts.append([1, pm+1])
            if rem > 0:
                new_parts.append([rem, 1])
        return normalize(new_parts), exclude, add, remainder

    k_prev, p_prev = partition[-2]
    exclude = f"{k_prev}*{p_prev}, 1*{pm}"
    add = f"1*{p_prev+1}"
    total = k_prev * p_prev + pm
    rem = total - (p_prev + 1)
    remainder = f"{rem}*1" if rem > 0 else "0"
    new_parts = partition[:-2]
    new_parts.append([1, p_prev+1])
    if rem > 0:
        new_parts.append([rem, 1])
    return normalize(new_parts), exclude, add, remainder

def generate(n):
    partition = [[n, 1]]
    headers = ("мультиразбиение", "исключить", "добавить", "остаток")
    col_widths = (35, 12, 12, 10)
    sep = " | "
    header_line = sep.join(h.ljust(w) for h, w in zip(headers, col_widths))
    print(header_line)
    print("-" * len(header_line))

    while True:
        if partition == [[1, n]]:
            star_str = to_star(partition)
            exp_str = expanded(partition)
            first_col = f"{star_str} = {exp_str}"
            print(f"{first_col:<{col_widths[0]}} | {'-':>{col_widths[1]}} | {'-':>{col_widths[2]}} | {'-':>{col_widths[3]}}")
            break

        new_part, exclude, add, remainder = next_step(partition)

        star_str = to_star(partition)
        exp_str = expanded(partition)
        first_col = f"{star_str} = {exp_str}"
        print(f"{first_col:<{col_widths[0]}} | {exclude:>{col_widths[1]}} | {add:>{col_widths[2]}} | {remainder:>{col_widths[3]}}")

        partition = new_part

if __name__ == "__main__":
    generate(10)
