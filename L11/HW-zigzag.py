n = int(input())
lst = [[0]*n for i in range(n)]
nub = 1
i = n-1
j = 0
ch = -1
p = -1
s = 0
for k in range(n**2):
    if j < 0:
        p = 1
        j+=p
        ch = 1
    if i<0:
        if n%2 == 0:
            ch = 1
            p = 2
            i+=ch
            j = j+p
            p=1
        else:
            if s == 0:
                ch = 1
                i+=ch
                s = 1
                j = j+s
                p = 1
                s = 2
            elif s == 2:
                ch = 1
                i+=ch
                j = j+s
                p = 1
                s = 2  
    if j>=n:
        p = -1
        j+=p
        ch = -1
        i = i+ch+p
    if i>=n:
        ch = -1
        i+=ch
        p = -1
    #print(i,j,nub,ch,p)
    lst[i][j] = nub
    i+=ch
    j+=p
    nub+=1
for i in range(n):
    for j in range(n):
        print(f'{lst[i][j]:3.0f}',end=' ')
    print()
    





        

    