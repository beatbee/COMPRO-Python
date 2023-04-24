n = int(input("N : "))
color = [int(x) for x in input().split()]
ch = 0
for i in range(len(color)-1):
    if color[i] == 1:
        for j in range(i+2,n,2):
            if color[j] == 2:
                print('no')
                ch = 1
                break
    if color[i] == 2:
        for j in range(i+2,n,2):
            if color[j] == 1:
                print('no')
                ch = 1
                break
    if color[i] == 0:
        continue
if ch==0: print('yes')


 