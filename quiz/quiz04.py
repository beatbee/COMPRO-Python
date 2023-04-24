file = input('filename: ')
data1 = []
data2 = {}
with open(file,'r') as fp:
    header = fp.readline().strip().split(',')
    for i in fp.read().strip().split('\n'):
        data = {}
        w = i.strip().split(',')
        for j in range(len(header)):
            if j == 0:
                data[header[j]] = w[j]
            else:
                data[header[j]] = int(w[j])
        data1.append(data)
        for j in range(5,len(header)):
            if w[0] not in data2:
                data2[w[0]] = [int(w[j])]
            else:
                data2[w[0]].append(int(w[j]))
n = int(input('type: '))
if n == 1:
    ans = 0
    for i in data1:
        ans+=i['Total Cases']
    print(ans)
elif n == 2:
    mx = -1
    ans = ''
    for i in data1:
        if i['Total Cases'] > mx:
            mx = i['Total Cases']
            ans = i['State/UTs']
    print(ans)
elif n == 3:
    mx = -1
    ans = ''
    for i in data1:
        if (i['Deaths']/i['Total Cases'])*100 > mx:
            mx = (i['Deaths']/i['Total Cases'])*100
            ans = i['State/UTs']
    print(ans)
elif n == 4:
    mx = -1
    ans = ''
    for i in data1:
        if (i['Discharged']/i['Total Cases'])*100 > mx:
            mx = (i['Discharged']/i['Total Cases'])*100
            ans = i['State/UTs']
    print(ans)
elif n == 5:
    ans = 0
    total = 0
    for i in data1:
        ans+= i['Active']
        total += i['Total Cases']
    print(f'{(ans/total)*100:.2f}%')
elif n == 6:
    D = {}
    lst = []
    newD = {}
    for i in data2:
        D[i] = sum(data2[i])/7
    for i in D.values():
        lst.append(i)
    for j in sorted(lst,reverse=True):
        for k,l in D.items():
            if l == j:
                newD[k] = l
    ch = 0
    for i,j in newD.items():
        if ch == 5:
            break
        else:
            print(f'{i} {j:.0f}')
        ch+=1
elif n == 7:
    D= {}
    newD = []
    for i in data2:
        for k in range(3):
            ch = 0
            for j in range(k,k+5):
                if data2[i][j] > 100:
                    ch+=1
            if ch >= 5:
                if i in newD:
                    pass
                else:
                    newD.append(i)
    for i in sorted(newD):
        print(i)
elif n == 8 :
    ans = []
    for state in data1:
        ch = 0 
        if state['day3'] > 100 and state['day4'] > 100 and state['day5'] > 100 :
            if state['day1'] > 100 and state['day2'] > 100 : ans.append(state['State/UTs'])
            elif state['day2'] > 100 and state['day6'] > 100 : ans.append(state['State/UTs'])
            elif state['day6'] > 100 and state['day7'] > 100 : ans.append(state['State/UTs'])
    ans.sort()
    print('\n'.join(ans))


    



                



        