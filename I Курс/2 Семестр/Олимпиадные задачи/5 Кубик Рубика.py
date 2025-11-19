for u in [f"{i:02}" for i in range(1, 21)]:
    file = open(f"OLYMP\Cube\input_s1_{u}.txt")
    file_out = open(f"OLYMP\Cube\output_s1_{u}.txt").readline()
    line = file.readline().strip()
    n, m = map(int, line.split())
    line = file.readline().strip()
    xPos, yPos, zPos = map(int, line.split())
    for _ in range(m):
        line = file.readline().strip()
        axis, cord, dir = line.split()
        cord = int(cord)
        dir = int(dir)
        if axis == "X":
            if xPos == cord:
                if dir > 0:
                    tmp = zPos
                    zPos = n + 1 - yPos
                    yPos = tmp
                else:
                    tmp = yPos
                    yPos = n + 1 - zPos
                    zPos = tmp
        elif axis == "Y":
            if yPos == cord:
                if dir > 0:
                    tmp = zPos
                    zPos = n + 1 - xPos
                    xPos = tmp
                else:
                    tmp = xPos
                    xPos = n + 1 - zPos
                    zPos = tmp
        elif axis == "Z":
            if zPos == cord:
                if dir > 0:
                    tmp = yPos
                    yPos = n + 1 - xPos
                    xPos = tmp
                else:
                    tmp = xPos
                    xPos = n + 1 - yPos
                    yPos = tmp
    print(f"{xPos} {yPos} {zPos}")
    if f"{xPos} {yPos} {zPos}" == file_out:
        print("True")
    else:
        print("False")
