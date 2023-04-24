n = int(input())
for i in range(1,n//2 +2):
    for k in range((n//2) +1 - i):
        print(end=' ')
    for j in range(2*i -1):
        print('O',end='')
    print()
for z in range(n//2+1,1,-1):
    for p in range(n//2 +2 -z):
        print(end=' ')
    for u in range(2*z-3):
        print('O',end='')
    print()
"""
for i in range(1, n+1, 2):
  print(' '*((n-i)//2), end='')
  print('O'*i)
for i in range(n-2, 0, -2):
  print(' '*((n-i)//2), end='')
  print('O'*i)
  
for i in range(1, n+1, 2):
  print(' '*((n-i)//2), end='')
  print('O'*i)
"""