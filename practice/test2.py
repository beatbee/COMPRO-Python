"""
def combi(s,l):
    lst = []
    if s == r:
        for i in range(r):
            lst.append(b[i])
        new.append(lst)
    else:
        for i in range(l+1,n+1):
            if a[i] == 0:
                a[i] =1
                b[s] = i
                combi(s+1,i)
                a[i] = 0
    return
r = 2
n = 3
new = []
a = [0]*(n+1)
b = [0]*(n+1)
combi(0,0)
print(new)
def combi(s,l):
    lst = []
    if s == r:
        for i in range(r):
            lst.append(b[i])
        new.append(lst)
    else:
        i = l+1
        for j in lst1:
            if a[j] == 0:
                a[j] = 1
                b[s] = j
                #print(b)
                combi(s+1,i)
                a[j] = 0
            i+=1
    return
r = 2
n = 3
lst1 = [1,2,3]
new = []
a = {}
for i in lst1:
    a[i] = 0
b = [0]*(n+1)
combi(0,0)
print(new)
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
