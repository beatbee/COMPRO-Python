file = input('Filename : ')
lst = []
with open(file,'r') as fp:
    s = fp.read()
    for i in s.split('\n'):
        if i != '' and i!='No,Height,Cost':
            w = i.split(',')
            if int(w[1]) > 8 and int(w[2]) > 75000:
                lst.append(int(w[0]))
            elif int(w[1]) <= 8 and int(w[2]) > 30000:
                lst.append(int(w[0]))
            elif int(w[1]) <= 4 and int(w[2]) > 5000:
                lst.append(int(w[0]))
            elif int(w[1]) <= 1 and int(w[2]) > 1000:
                lst.append(int(w[0]))
if lst == []:
    print('No')
else:
    print('Yes')
    for i in sorted(lst):
        print(i)
            


