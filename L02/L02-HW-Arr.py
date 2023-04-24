n = int(input())
a = input('Arrow : ')
s = input('Stick : ')
for i in range(1,n+1):
    for k in range(n-i+1):
        print(end=' ')
    for j in range(2*i-1):
        print(a,end='')
    print()
for i in range(1,n+1):
    print(' '*(n-1),s)
"""
for i in range(n,0,-1):
  print(' '*i + A*(2*(n-i+1)-1))
for i in range(n):
  print(' '*n + B)
"""   