"""
def isPrime(num):
    ch = 0
    if num == 1 or num == 0:
        return None
    else:
        ans = 0
        for i in range(2,num):
            if  num%i == 0:
                ans+=1
        if  ans > 0 and num!=2:
            return None          
        elif(num == 2):
            return num
        else:
            return num
lst = []
cnt = 0
while(True):
    n = int(input())
    if n==0:
        break
    x = isPrime(n)
    if x != None:
        lst.append(x)
for i in lst:
    print(i,end=' ')
    cnt+=1
    if cnt %10 == 0:
        print() 
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
    for i in range(n+1):
        if mark[i] == False :
            prime.append(i)                  
lst = []
num = []
prime = []           
while(True):
    n = int(input())
    if n==0:
        break
    num.append(n)
x = max(num)
isPrime(x)
cnt = 0 
for i in num:
    if i in prime:
        cnt+=1
        print(i,end=' ')
    if cnt == 10:
        print()
        cnt = 0
    

    
            


      
