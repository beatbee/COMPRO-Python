lst = []
while True:
    n = input('Input student score (or just ENTER to end): ')
    if n == '':
        break
    else:
        x = int(n)
        lst.append(x)
x = sorted(lst)
j = 1
for i in range(len(x)-1,-1,-1):
    print(f'Rank #{j}: {x[i]}')
    j+=1
