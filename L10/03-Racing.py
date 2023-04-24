"""
import json
class Racing:
    def __init__(self,name,rangee,velocity,response):
        self.name = name ; self.rangee = rangee ; self.velocity = velocity ; self.response = response
file = input('Enter json filename : ')
with open(file,'r') as fp:
    yes= fp.read()
s = json.loads(yes)
classes = []
for i in s['racer']:
    name,rangee,velocity,response = i['name'],i['_range'],i['velocity'],i['response']
    data = Racing(name,rangee,velocity,response)
    classes.append(data)
d = int(input('Enter distance (meter) : '))
lst = {}
res = {}
time = []
res2 = {}
time1 = {}
name = []
res3 = []
for i in classes:
    ans = 0
    ch = 0
    cnt = 0
    for j in range(len(i.rangee)):
        if i.name == 'D':
            ans = d/i.velocity[0]
        elif j == len(i.rangee)-1 or (j == len(i.rangee)-2 and d<i.rangee[len(i.rangee)-1]):
            if j == len(i.rangee)-1 and d < i.rangee[len(i.rangee)-1]:
                break
            cnt = abs(d - i.rangee[j])
            ans+=cnt/i.velocity[j]
        elif d>= i.rangee[j+1]:
            ans += (i.rangee[j+1]-ch)/i.velocity[j]
            ch = i.rangee[j+1]
    lst[i.name] = f'{ans:.2f}'
    res[i.name] = i.response
    res3.append(i.response)
    name.append(i.name)
name = sorted(name)
for i in lst:
    lst[i] = float(lst[i])
    if lst[i] not in time:
        time.append(lst[i])
        time1[lst[i]] = 1
    else:
        time1[lst[i]] += 1
for i in sorted(res3,reverse=True):
    if i not in res2:
        res2[i] = 1
    else:
        res2[i] +=1
for i in sorted(time):
    if time1[i] > 1:
        for k in res2:
            if res2[k] == 1:
                for j in lst:
                    if lst[j] == i:
                        if res[j] == k:
                            print(f'{j} {lst[j]:.2f}')
            else:
                for n in name:
                    for j in lst:
                        if lst[j] == i and res[j] == k:
                            if j == n:
                                print(f'{j} {lst[j]:.2f}')
    else:
        for j in classes:
            if lst[j.name] == i:
               print(f'{j.name} {lst[j.name]:.2f}') 
"""
import json
class Racing:
    def __init__(self,name,rangee,velocity,response,ans):
        self.name = name ; self.rangee = rangee ; self.velocity = velocity ; self.response = response ; self.time = ans
    def __lt__(self,other):
        if self.time != other.time: return self.time<other.time
        elif self.response != other.response: return self.response > other.response
        else: return self.name < other.name
file = input('Enter json filename : ')
with open(file,'r') as fp:
    yes= fp.read()
s = json.loads(yes)
d = int(input('Enter distance (meter) : '))
classes = []
for i in s['racer']:
    name,rangee,velocity,response = i['name'],i['_range'],i['velocity'],i['response']
    ans = 0
    ch = 0
    cnt = 0
    for j in range(len(i['_range'])):
        if i['name'] == 'D':
            ans = d/i['velocity'][0]
        elif j == len(i['_range'])-1 or (j == len(i['_range'])-2 and d<i['_range'][len(i['_range'])-1]):
            if j == len(i['_range'])-1 and d < i['_range'][len(i['_range'])-1]:
                break
            cnt = abs(d - i['_range'][j])
            ans+=cnt/i['velocity'][j]
        elif d>= i['_range'][j+1]:
            ans += (i['_range'][j+1]-ch)/i['velocity'][j]
            ch = i['_range'][j+1]
    data = Racing(name,rangee,velocity,response,ans)
    classes.append(data)
classes.sort()
for i in classes:
    print(f'{i.name} {i.time:.2f}')


            
            
