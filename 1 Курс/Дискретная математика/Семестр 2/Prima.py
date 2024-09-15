# Прима (Ответ: 38)
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
sum_weight = 0
tree = []
for i in graf:
    if not (i[0] in tree): tree.append(i[0])
    if not (i[1] in tree): tree.append(i[1])
new_tree = [tree[0]]
pos_ways = []
while len(new_tree) != len(tree):
    for x in range(len(graf)):
        for u in new_tree:
            if ((u == graf[x][0] and not (graf[x][1] in new_tree)) or (u == graf[x][1] and not (graf[x][0] in new_tree))) and not (graf[x] in pos_ways):
                pos_ways.append(graf[x])
    pos_ways = sorted(pos_ways, key=lambda x: x[2])
    del_ways = []
    for i in pos_ways:
        if i[0] in new_tree and i[1] in new_tree:
            del_ways.append(i)
    for i in del_ways:
        pos_ways.remove(i)
    minim = pos_ways[0]
    if not minim[0] in new_tree:
        new_tree.append(minim[0])
    else:
        new_tree.append(minim[1])
    sum_weight += minim[2]
    pos_ways.remove(minim)
    graf.remove(minim)
print(sum_weight)