file = input('File name: ')
D = {}
userid = {}
with open(file,'r') as fp:
    header = fp.readline()
    x = header.split(',')
    j = 0
    for i in fp.read().split(','):
        D[x[j]] = []
        D[x[j]].append(i)
        j+=1
print(D)
