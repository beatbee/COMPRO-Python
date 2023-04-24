import json
file = input('Filename : ')
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
tpe = input('type : ')
D = {}
for i in s:
    if i['species'] not in D:
        D[i['species']] = 1
    else:
        D[i['species']] += 1
new = {}
for k in D:
    for i in s:
        if i['species'] == k:
            for j in i:
                if j == tpe:
                    if k not in new:
                        new[k] = i[j]
                    else:
                        new[k] += i[j]
for i,j in new.items():
    print(f'{i} = {j/D[i]:.2f}')



