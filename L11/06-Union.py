def union(a,b):
    lst = b
    for i in a:
        if i in lst:
            continue
        else:
            lst.append(i)
    return lst
A = [int(x) for x in input('Input set A: ').split()]
B = [int(x) for x in input('Input set B: ').split()]
res = union(A,B)
print(f'A union B: {sorted(res)}')