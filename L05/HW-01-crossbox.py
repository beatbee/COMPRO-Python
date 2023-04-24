n = int(input())
print('.'*n)
j = n-2
for i in range(n//2-1):
    print('.'+' '*i+'.'+' '*(j-2) + '.'+' '*i +'.')
    j-=2
print('.'+' '*(n//2-1)+'.'+' '*(n//2-1)+'.')
j = 3
for i in range(n//2-2,-1,-1):
    print('.'+' '*i+'.'+' '*(j-2) + '.'+' '*i +'.')
    j+=2
print('.'*n)
