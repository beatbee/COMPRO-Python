def minus(a,b):
    lst = []
    for i in a:
        if i not in b:
            lst.append(i)
    if lst == []:
        return 'empty set'
    return lst
A = [int(x) for x in input('Input set A: ').split()]
B = [int(x) for x in input('Input set B: ').split()]
res = minus(A,B)
print(f'A minus B: {res}')


