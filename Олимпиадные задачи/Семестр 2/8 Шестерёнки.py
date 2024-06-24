def Prog(input_path=None):
    def sig(a):
        return (a > 0) - (a < 0)

    with open(input_path, "r") as f:
        N, M = map(int, f.readline().strip().split())
        gears = [list(map(int, f.readline().strip().split())) for _ in range(N)]
        connections = [list(map(lambda x: int(x) - 1, f.readline().strip().split())) for _ in range(M)]
        Z1, Z2 = map(lambda x: int(x) - 1, f.readline().strip().split())
        V = int(f.readline().strip())
    gears.sort()
    connections.sort()
    gears[Z1].append(V)
    for i in range(len(gears)):
        if i != Z1:
            gears[i].append(0)
    for c1, c2 in connections:
        if gears[c1][2] != 0 and gears[c2][2] == 0:
            gears[c2][2] = -gears[c1][2] * gears[c1][1] / gears[c2][1]
        elif gears[c1][2] == 0 and gears[c2][2] != 0:
            gears[c1][2] = -gears[c2][2] * gears[c2][1] / gears[c1][1]
        elif gears[c1][2] != 0 and gears[c2][2] != 0:
            if sig(gears[c1][2]) == sig(gears[c2][2]):
                gears[Z2][2] = 0
                break
    if gears[Z2][2] != 0:
        q = f"{abs(round(gears[Z2][2], 3)):.3f}"
        out_str = f"1\n{sig(gears[Z2][2])}\n{q}"
    else:
        out_str = "-1"
    return out_str

print(Prog("OLYMP/- Gears/input_s1_13.txt"))
# Не работает только 13 тест