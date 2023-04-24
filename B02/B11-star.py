n = int(input("n: "))
for i in range(1,n//2+1):
    print(' '*(i-1),end='')
    print('+'+' '*(n//2-i)+'+'+' '*(n//2-i)+'+')
print('+'*n)
for i in range(1,n//2+1):
    print(' '*(n//2-i),end='')
    print('+'+' '*(i-1)+'+'+' '*(i-1)+'+')