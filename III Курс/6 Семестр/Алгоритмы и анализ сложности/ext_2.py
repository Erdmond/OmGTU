def sliding_window(arr, k, mode="min"):
    head, tail = [], []
    cmp = min if mode == "min" else max
    neutral = float('inf') if mode == "min" else float('-inf')
    results = []

    def push(stack, val):
        if not stack: stack.append((val, val))
        else: stack.append((val, cmp(val, stack[-1][1])))

    def get_extreme(stack):
        return stack[-1][1] if stack else neutral

    def fmt(st):
        return "; ".join(f"{v}/{m}" for v, m in st) if st else ""

    print(f"{'tail':<25} | {'подмассив':<15} | {'результат':<25} | {'head'}")
    print("-" * 90)

    for i, val in enumerate(arr):
        push(tail, val)
        
        if i >= k:
            if not head:
                while tail:
                    v, _ = tail.pop()
                    push(head, v)
            if head:
                head.pop()

        if i >= k - 1:
            sub = arr[i-k+1 : i+1]
            cur = cmp(get_extreme(head), get_extreme(tail))
            results.append(cur)
            res_str = " ".join(map(str, results))
        else:
            sub = arr[:i+1]
            res_str = ""

        print(f"{fmt(tail):<25} | {' '.join(map(str, sub)):<15} | {res_str:<25} | {fmt(head)}")


if __name__=='__main__':
    A = [11, 18, 14, 3, 5, 17, 4, 15, 6, 17, 25, 3, 14, 1, 5, 47, 6, 13, 20, 23, 6, 13]
    sliding_window(A, k=5, mode="min")
