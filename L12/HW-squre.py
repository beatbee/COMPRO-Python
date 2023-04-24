def cou(l,i,j):
    cnt = 0
    cnt1 = 0
    for a in range(i,i+l):
        for b in range(j,j+l):
            if a < r and b < c:
                cnt+=1
    if cnt == l*l:
        cnt1 = 1
    return cnt1
r = int(input('R: '))
c = int(input('C: '))
mn = min(r,c)
ans = 0
for k in range(1,mn+1):
    for i in range(r):
        for j in range(c):
            ans += cou(k,i,j)
print(ans)

