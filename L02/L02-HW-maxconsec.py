"""
ans = 0
p = 0
while(True):
    n = int(input())
    if(n == 0):
        break
    if(p == 0):
        p = 1
        ch = 1
        q = n
    if(ans == n):
        ch+=1
        if(ch>p):
            p = ch
            q = n
    elif ans != n:
        ch  = 1
    ans = n
print(p)
print(q)
"""
freq = 0
ch = 0
num = 0
ans = 0
while(True):
    n = int(input())
    if n == 0:
        break
    if num == 0:
        num = 1
        ans = n
        freq = n
    if n == freq:
        ch+=1
        if ch>num:
            num = ch 
            ans = n
    else:
        ch = 1
    freq = n
print(num)   
print(ans)


    







    