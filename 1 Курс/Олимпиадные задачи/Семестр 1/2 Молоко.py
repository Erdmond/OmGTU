f = open('input7.txt').readlines()
xyz = []
for j in range(len(f) - 1):
    xyz.append(f[j+1].split())
minmilk = []
for a in xyz:
    x1 = float(a[0])
    y1 = float(a[1])
    z1 = float(a[2])
    x2 = float(a[3])
    y2 = float(a[4])
    z2 = float(a[5])
    price1 = float(a[6])
    price2 = float(a[7])
    s1 = (x1 * y1 + x1 * z1 + y1 * z1) * 2
    s2 = (x2 * y2 + x2 * z2 + y2 * z2) * 2
    v1 = x1 * y1 * z1
    v2 = x2 * y2 * z2
    milk = round((price2 * s1 - price1 * s2) / (s1 * v2 - s2 * v1) * 1000, 2)
    minmilk.append(milk)
minim = min(minmilk)
print(minmilk.index(minim)+1, minim)
