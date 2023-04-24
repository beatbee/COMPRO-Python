import json
file = input('Filename : ')
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
name = input('Data : ')
ch = 0
for i in s:
    for b in i:
        if i[b] == name:
            print('Found in blacklist')
            for j,k in i.items():
                print(f'{j} : {k}')
                ch = 1
if ch == 0:
    print('Not found in blacklist')

        