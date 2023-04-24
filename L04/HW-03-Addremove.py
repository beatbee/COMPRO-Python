lst = list(map(int,input().split()))
while(True):
    menu,x = input().split()
    x = int(x)
    if menu == 'E':
        break
    if menu == 'A':
        lst.append(x)
    if menu == 'S':
        print(lst[x])
    if menu == 'R':
        lst.remove(lst[x])
for i in lst:
    print(i,end=' ')


