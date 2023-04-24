s = ''
with open('test.txt','r') as fp:
    s = fp.read()
x = ''
with open('test1.txt','r') as ct:
    x = ct.read()
eu = {}
cnt1 = 0
hello = []
for i in x.split('\n'):
    if i != '' and i !='country,population,EU,coastline':
        w = i.split(',')
        v = {}
        v['country'] = w[0]
        v['population'] = w[1]
        v['EU'] = w[2]
        v['coastline'] = w[3]
        hello.append(v)
#print(hello[0]['EU'])
for i in range(len(hello)):
    if hello[i]['EU'] == 'yes':
        x = hello[i]['country']
        y = hello[i]['population']
        print(f'{x} pop = {float(y):.2f}')      
        cnt1+=1
cn = {}
cnt = {}
for i in range(len(hello)):
    x = hello[i]['country'][0]
    y = hello[i]['population']
    if hello[i]['country'][0] in cn:
        cn[x]+=float(y)
    else:
        cn[x]=float(y)
for i in cn:
    print(f'{i} : {cn[i]:.2f}')
"""
for i in s.split('\n'):
    if i!='city,country,latitude,longitude,temperature' and i!= '':
        w = i.split(',')
        if w[1] in cn:
            cn[w[1]]+=float(w[4])
            cnt[w[1]] += 1
        else:
            cn[w[1]] = float(w[4])
            cnt[w[1]] = 1
for i,j in cn.items():
    j = j/cnt[i]
    #print(i,j)
temeu = 0  
for i in s.split('\n'):
    if i!='city,country,latitude,longitude,temperature' and i!= '':
        w = i.split(',')
        if w[1] in eu:
            temeu+=float(w[4])
#print(temeu/cnt1)
"""
x = ''
with open('test1.txt','r') as ct:
    x = ct.read()
eu = {}
cn = {}
co = {}
cnt = {}
for i in x.split('\n'):
    if i != '' and i !='country,population,EU,coastline':
        w = i.split(',')
        n = w[0]
        cn[n] = float(w[1])
#print(cn)
for i in x.split('\n'):
    if i != '' and i !='country,population,EU,coastline':
        w = i.split(',')
        if w[2] == 'yes':
            n = w[0]
            eu[n] = float(w[1])
total = sum(eu.values())
print(total)
co = 0
for i in x.split('\n'):
    if i != '' and i !='country,population,EU,coastline':
        w = i.split(',')
        if w[3] == 'yes':
            co +=1
print(co)
for i,j in cn.items():
    if i[0] in cnt:
        cnt[i[0]]+=j
    else:
        cnt[i[0]] = j
print(cnt)
hell = {}
for i,j in cn.items():
    if j > 50:
        hell[i] = j
happy = dict(sorted(hell.items(), key=lambda item: item[1], reverse=True))
print(happy)

        



     
