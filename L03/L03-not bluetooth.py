n = input()
n= n.upper()
if n[0] == n[len(n)-1]:
    print('YES')
    print(n[0])
else:
    print('NO')