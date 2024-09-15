MaxN = int(input())
out = 0
for x in [2 ** n for n in range(1, 100)]:
    out += int((MaxN / (x - 1)))
print(out)
