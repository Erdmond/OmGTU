# Крускал (Ответ: 38)
"""
8
14
A B 2
A C 2
A E 7
B C 2
B E 2
B D 9
C E 5
E D 10
E G 9
D G 2
D H 16
D F 5
G H 17
F H 17
"""
points = int(input())
lines = int(input())
graf = []
for i in range(lines):
    graf.append(input().split())
for i in range(len(graf)):
    graf[i][2] = int(graf[i][2])
graf = sorted(graf, key=lambda x: x[2])
sum_weight = 0
tree = []
for i in graf:
    if not (set(i[0]) in tree): tree.append(set(i[0]))
    if not (set(i[1]) in tree): tree.append(set(i[1]))
k = 0
while len(tree) != 1:
    for x in range(len(tree)):
        if graf[k][0] in tree[x]: a = tree[x]; break
    for y in range(len(tree)):
        if graf[k][1] in tree[y]: b = tree[y]; break
    if a != b:
        sum_weight += graf[k][2]
        tree.append(set(a).union(set(b)))
        tree.remove(set(a))
        tree.remove(set(b))
    k += 1
print(sum_weight)
