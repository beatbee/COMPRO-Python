import math
def printMat(m):
  s = '   '
  for i in range(len(m)):
    s += f'{i+1:<3}'
  s += '\n'
  for i in range(len(m)):
    for j in range(len(m[i])):
      if j==0:
        s +=f'{i+1:^3}'
      s += f"{m[i][j]:3}"
    s += '\n'
  print(s)
def check(l):
    n = int(math.sqrt(l))+1
    mn = 10000
    ch = []
    ans = 0
    for i in range(1,n):
        for j in range(1,n+1):
            if i*j <= l :
                ch.append(j-i)
                if min(ch) <mn:
                    mn = min(ch)
                    ans = i
    return ans+1
def type1(s):
    n = check(len(s))
    x = list(s)
    lst = [['*']*n for i in range(n)]
    a = 0
    for i in range(n):
        for j in range(n):
            if a > len(s):
                lst[i][j] == '*'
            elif a<len(s):
                lst[i][j] = s[a]
            a+=1
    return lst
def type2(s):
    n = check(len(s))
    x = list(s)
    lst = [['*']*n for i in range(n)]
    a = 0
    for i in range(n):
        for j in range(n):
            if a > len(s):
                lst[j][i] == '*'
            elif a<len(s):
                lst[j][i] = s[a]
            a+=1
    return lst
def type3(s):
    n = check(len(s))
    x = list(s)
    lst = [['*']*n for i in range(n)]
    a = 0
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if a > len(s):
                lst[i][j] == '*'
            elif a<len(s):
                lst[i][j] = s[a]
            a+=1
    return lst
def type4(s):
    n = check(len(s))
    x = list(s)
    lst = [['*']*n for i in range(n)]
    a = 0
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if a > len(s):
                lst[j][i] == '*'
            elif a<len(s):
                lst[j][i] = s[a]
            a+=1
    return lst
def type5(s):
    n = check(len(s))
    x = list(s)
    lst = [['*']*n for i in range(n)]
    a = 0
    for i in range(n):
        for j in range(n):
            if a > len(s):
                lst[i][j] == '*'
            elif a<len(s):
                lst[i][j] = s[a]
            a+=1
    return lst

print('Enter a sentence or pharse and then press ENTER')
s = input()
n = int(input("Enter output type (only 1..5:) "))
if n==1:
  res = printMat(type1(s))
elif n==2:
  res = printMat(type2(s))
elif n==3:
  res = printMat(type3(s))
elif n==4:
  res = printMat(type4(s))
elif n==5:
  res = printMat(type5(s))
