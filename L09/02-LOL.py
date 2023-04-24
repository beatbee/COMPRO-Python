import json
file = input('Filename : ')
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
case = int(input('Case : '))
if case == 0:
    c = [int(x) for x in input('Character : ').split(',')]
    for i in s:
        if s[i]['id'] in c:
            x = s[i]['name']
            y = s[i]['id']
            z = s[i]['title']
            print(f'{y}\t---\t{x}\t---\t{z}\t')
elif case == 1:
    c = [x for x in input('Character : ').split(',')]
    for i in s:
        if s[i]['name'][0] in c:
            x = s[i]['name']
            y = s[i]['id']
            z = s[i]['title']
            print(f'{y}\t---\t{x}\t---\t{z}\t')
elif case == 2:
    c = [x for x in input('Character : ').split(',')]
    for i in s:
        j = 0
        if s[i]['title'][:3] == 'the' or s[i]['title'][:3] == 'The':
            j = 4
        if s[i]['title'][j] in c:
            x = s[i]['name']
            y = s[i]['id']
            z = s[i]['title']
            print(f'{y}\t---\t{x}\t---\t{z}\t')
    
#championinfo.json