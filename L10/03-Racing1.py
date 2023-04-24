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