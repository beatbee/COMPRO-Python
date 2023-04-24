file = input('Enter your Filename: ')
op = input('Show by name or id?: ')
p = int(input('How many similarity percentages do you want?: '))
num = int(input('Input number of top similarity: '))
data = {}
lst = []
new = []
with open(file,'r') as fp:
    header = fp.readline()
    s = fp.read()
    for i in s.strip().split('\n'):
        w = i.strip().split(',')
        lst = []
        for j in range(len(w)):
            lst.append(w[j])
        new.append(lst)
h = []
corr = []
check = []
if op == 'name':       
    for i in new:
        h = []
        if float(i[2]) >= p :
            if len(check) == 0:
                h.append(i[1])
                h.append(i[4])
            elif len(check) == 1 and i[1] not in check and i[4] not in check:
                print('wat')
                h.append(i[1])
                h.append(i[4])
            for j in new:
                if i[1] == j[1] and j[4] not in h and float(j[2]) >= p:
                    h.append(j[4])
                if i[4] == j[1] and j[4] not in h and float(j[2]) >= p:
                    h.append(j[4])
                if i[1] == j[4] and j[1] not in h and float(j[2]) >= p:
                    h.append(j[1])
                if i[4] == j[4] and j[1] not in h and float(j[2]) >= p:
                    h.append(j[1])
        check = h
        corr.append(h)
        #h = []
if op == 'id':       
    for i in new:
        h = []
        if float(i[2]) >= p :
            if len(check) == 0:
                h.append(i[0])
                h.append(i[3])
            elif len(check) == 1 and i[0] not in check and i[3] not in check:
                print('wat')
                h.append(i[0])
                h.append(i[3])
            for j in new:
                if i[0] == j[0] and j[3] not in h and float(j[2]) >= p:
                    h.append(j[3])
                if i[3] == j[0] and j[3] not in h and float(j[2]) >= p:
                    h.append(j[3])
                if i[0] == j[3] and j[0] not in h and float(j[2]) >= p:
                    h.append(j[0])
                if i[3] == j[3] and j[0] not in h and float(j[2]) >= p:
                    h.append(j[0])
        check = h
        corr.append(h)
c=1
for i in range(0,len(corr)):
    print(f'Group{c}: {" ".join(corr[i])}')
    c+=1



    

        
