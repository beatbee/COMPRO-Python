def Head(n):
    print(' '+'o'*n)
    for i in range(n//2 -1):
        print(' ' + 'o' + ' '*(n-2) + 'o')
    print(' '+'o'*n)
def Body(n):
    for i in range(1,n):
        if i == n//2:
            print('-'*(n//2) + '||' +'-'*(n//2))
        else:
            print(' '*(n//2) + '||')
def Leg(n):
    j = 0
    for i in range((n//2+1),1,-1):
        print(' '*(i-1) + '/'+' '*(j)+"\\")
        j+=2

n = int(input())
Head(n)
Body(n)
Leg(n)