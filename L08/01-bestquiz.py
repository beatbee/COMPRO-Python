stu = {}
name = input('File name: ')
with open(name, 'r') as fp:
    #s = fp.read()
    for i in fp.readlines():
        lst = []
        w = i.split(' ')
        for j in range(1,len(w)):
            lst.append(int(w[j]))
        stu[w[0]] = lst
mx = -1
for i in stu.values():
    i.remove(max(i))
    i.remove(min(i))
    i = sum(i)
    if i>mx:
        mx = i
print(mx)
for i,j in stu.items():
    j = sum(j)
    if j == mx:
        print(i)                