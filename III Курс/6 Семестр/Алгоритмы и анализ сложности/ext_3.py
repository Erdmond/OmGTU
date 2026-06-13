def partitions(n):
    def gen(rem, k, min_part):
        if k == 1:
            if rem >= min_part:
                yield [rem]
            return
        for first in range(min_part, rem // k + 1):
            for tail in gen(rem - first, k - 1, first):
                yield [first] + tail

    for length in range(1, n + 1):
        yield from gen(n, length, 1)


if __name__ == "__main__":
    n = 10
    for p in partitions(n):
        print(f"{n} = " + " + ".join(map(str, p)))
