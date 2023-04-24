p = int(input("pattern: "))
c = input("char: ")
n = int(input("n: "))
if p == 1:
    for i in range(1,n+1):
        print(c*i,end='\n')
elif p == 2:
    for i in range(n,0,-1):
        print(c*i,end='\n')
elif p == 3:
    j = n-1
    for i in range(1,n+1):
        print(' '*j + c*i,end='\n')
        j-=1
elif p == 4:
    j = 0
    for i in range(n,0,-1):
        print(' '*j+c*i,end='\n')
        j+=1