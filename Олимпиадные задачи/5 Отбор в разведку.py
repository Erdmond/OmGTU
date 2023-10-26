arr = [0, 0, 0, 1]
f = int(open('OLYMP/Отбор в разведку/input_s1_10.txt').readline())
for i in range(4, f + 1):
    arr.append(arr[(i + 1) // 2] + arr[i // 2])
print(arr[f])
