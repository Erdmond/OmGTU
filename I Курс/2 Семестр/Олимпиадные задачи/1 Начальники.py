def add_pers(num, name):
    Persons[num] = name
def find_slaves(mast, base):
    slaves = set()
    for y in range(len(base) - 1):
        if y % 2 == 0 and base[y][0] == mast:
            slaves.add(base[y + 1][0])
    return slaves

Persons = {}
f = open("OLYMP/Company/input_s1_16.txt").readlines()
IDs = set([i[:4] for i in f][:-2])
Pers = []

for i in range(len(f) - 2):
    Pers.append([f[i][:4], f[i][5:-1]])

for i in IDs:
    add_pers(i, 'Unknown Name')
    for u in Pers:
        if i == u[0] and u[1] != '':
            add_pers(i, u[1])


master = f[-1]
if not(master.isdigit()):
    for i in Pers:
        if i[1] == master:
            master = i[0]
            break

master_slaves = find_slaves(master, Pers)

new_slaves = set()
while True:
    lens = len(master_slaves)
    for u in master_slaves:
        new_slaves = new_slaves.union(find_slaves(u, Pers))
    master_slaves = master_slaves.union(new_slaves)
    if len(master_slaves) == lens:
        break

master_slaves = sorted(master_slaves)
if master_slaves == set():
    print("NO")
else:
    for o in master_slaves:
        print(o, Persons[o])