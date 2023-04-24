import math
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
def type5(s):
    n = check(len(s))
    x = list(s)
    lst = [['*']*n for i in range(n)]
    a = 0
    chup = 0
    chright = 0
    for i in range(n):
        for j in range(n):
            if a > len(s):
                lst[i][j] == '*'
            elif a<len(s):
                if j == 0 :
                    if chup == 0:
                        #lst[n-chup-1][j] = s[a]
                        print(n-chup-2,j,s[a])
                        chup+=1
                    else:
                        #lst[n-chup-1][j] = s[a]
                        print(n-chup-2,j,s[a])
                elif i == n-1:
                    if chright == 0:
                        #lst[i-chright][j] = s[a]
                        print(i-chright,j,s[a])
                        chright+=1
                    else:
                        #lst[i-chright][j] = s[a]
                        print(i-chright,j,s[a])
                #elif i>n-1:
                #elif j>n-1:
            a+=1
    return lst
s = input()
type5(s)