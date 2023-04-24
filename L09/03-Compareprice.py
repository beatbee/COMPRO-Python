import json
file = input('Filename : ')
data = input()
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
mn = 10000
ans = ''
for i in s:
    if i['Product type'] == data:
        if int(i['Cost']) < mn:
            mn = int(i['Cost'])
            ans = i['Brand']
print(f'{ans} : {mn}')