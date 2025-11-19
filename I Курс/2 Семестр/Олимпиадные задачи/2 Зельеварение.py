import re
f = [str(i).replace('\n','') for i in open('OLYMP/Alchemy/input10.txt').readlines()]
potion = {}
for i in range(len(f)):
    potion[i+1] = f[i]
def replace_key(rack):
    return potion[int(rack.group())]
for key in potion.keys():
    potion[key] = re.sub(r'\b\d+\b', replace_key, potion[key])
    if 'WATER ' in potion[key]:
        potion[key] = 'WT' + potion[key].replace('WATER', '') + ' TW'
    if 'DUST ' in potion[key]:
        potion[key] = 'DT' + potion[key].replace('DUST', '') + ' TD'
    if 'MIX ' in potion[key]:
        potion[key] = 'MX' + potion[key].replace('MIX', '') + ' XM'
    if 'FIRE ' in potion[key]:
        potion[key] = 'FR' + potion[key].replace('FIRE', '') + ' RF'
print(potion[len(f)].replace(' ', ''))
