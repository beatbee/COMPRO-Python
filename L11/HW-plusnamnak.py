def combi(lst,n):
    if n==0:
        return [[]]
    a=[]
    for i in range(0,len(lst)):
        m=lst[i]
        rest=lst[i+1:]
        for p in combi(rest,n-1):
            a.append([m]+p)
    return a
n = int(input('N : '))
D = {}
num= []
for i in range(n):
    a,b = [x for x in input().split()]
    b = int(b)
    D[b] = a
    num.append(b)
ans = int(input('XX : '))
res = []
ans1 =''
for i in range(n,0,-1):
    com = combi(num,i)
    for i in com:
        if sum(i) == ans:
            a = len(i)
            for j in range(a):
                res.append(D[i[j]])
print(' '.join(res))
"""
def combi(s,l):
    lst = []
    if s == r:
        for i in range(r):
            lst.append(b[i])
        new.append(lst)
    else:
        i = l+1
        for j in num:
            if a[j] == 0:
                a[j] = 1
                b[s] = j
                combi(s+1,i)
                a[j] = 0
            i+=1
    return new
n = int(input('N : '))
D = {}
num= []
new = []
a = {}
b = [0]*(n+1)
for i in range(n):
    x,y = [e for e in input().split()]
    y = int(y)
    D[y] = x
    num.append(y)
ans = int(input('XX : '))
for i in num:
    a[i] = 0
for i in range(1,n+1):
    r = i
    x = combi(0,0)
    for j in x:
        if sum(j) == ans:
            for k in j:
                print(D[k],end=' ')
            exit(0)
"""
"""
from itertools import combinations
n = int(input('N : '))
D = {}
num= []
for i in range(n):
    a,b = [x for x in input().split()]
    b = int(b)
    D[b] = a
    num.append(b)
ans = int(input('XX : '))
res = []
ans1 =''
for i in range(n,0,-1):
    com = combinations(num,i)
    for i in list(com):
        if sum(i) == ans:
            a = len(i)
            for j in range(a):
                res.append(D[i[j]])
print(' '.join(res))
"""


        


