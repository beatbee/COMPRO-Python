import json
file = input('File Name: ')
n = int(input('Input : '))
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
if n == 1:
    print(len(s))
elif n == 2:
    ans = 0
    for i in s:
        ans+=int(i['population'])
    print(ans)
elif n == 3:
    c = 0
    l = 0
    for i in s:
        if i['country'][0] == 'C':
            c+=1
        if len(i['country']) > 5:
            l+=1
    print(c)
    print(l)
elif n == 4:
    a = 0
    b = 0
    c = 0
    for i in s:
        if int(i['population']) > 500000000:
            a+=1
        if int(i['population']) > 250000000 and int(i['population']) > 750000000:
            b+=1
        if int(i['population']) < 10000000:
            c+=1
    print(a)
    print(b)
    print(c)
elif n == 5:
    ans = 0
    ch = 0
    for i in s:
        ch+=1
        if ch == 21:
            break
        ans+=float(i['World'])
    ans1 = 0
    for i in range(49,150):
        ans1 += float(s[i]['World'])
    print(f'{ans*100:.2f}')
    print(f'{ans1*100:.2f}')
"""
elif n == 6:
    total = 0
    ans = 0
    ans1 = 0
    for i in s:
        total += int(i['population'])
    for i in range(20):
        ans+=int(s[i]['population'])
    for i in range(49,150):
        print()
    print(f'{ans/total*100:.2f}')
"""


#worldpopulation.json