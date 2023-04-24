"""
def isPrime(num):
    if num == 1 or num == 0:
        return False
    else:
        ans = 0
        for i in range(2,num):
            if  num%i == 0:
                ans+=1
        if  ans > 0 and num!=2: return False          
        elif(num == 2): return num
        else: return num
n = int(input())
ans1 = n
ans2 = n+2
while (True):
    x = isPrime(ans1)
    y = isPrime(ans2)
    if x!=False and y!=False:
        ans1 = x
        ans = y
        break
    ans1+=1
    ans2+=1
print(f"({ans1}, {ans2})")
"""
import math
def isPrime(n):
    mark = [False]*(n+1)
    mark[0] = True
    mark[1] = True
    for i in range(2,int(math.sqrt(n)+1)):
        if not mark[i]:
            for j in range(i*i,n+1,i):
                mark[j] = True
    if mark[n] == False : return n
    else: return False
n = int(input())
ans1 = n
ans2 = n+2
while (True):
    x = isPrime(ans1)
    y = isPrime(ans2)
    if x!=False and y!=False:
        ans1 = x
        ans2 = y
        break
    ans1+=1
    ans2+=1
print(f"({ans1}, {ans2})")

    


