def printRegionMenu():
  s = '''List of Regions in Thailand
 1 - Central region
 2 - Eastern region
 3 - Lower northeastern region
 4 - Upper northeastern region
 5 - Upper northern region
 6 - Lower northern region
 7 - Western region
 8 - Upper southern region
 9 - Lower southern region'''
  print(s)
data = []
D = {}
with open('rainfall-2014-sampled.txt','r') as fp:
    s = fp.read()
    for i in s.strip().split('\n'):
        w = i.strip().split(',')
        D['date'] = w[6]
        D['location'] = w[2]
        x = w[2].split(' ')
        D['regcode'] = x[-1][0]
        D['rainfall'] = 0
        for j in range(7,len(w)):
            D['rainfall'] += float(w[j])
        data.append(D)
        D = {}
#print(data)        
printRegionMenu()
region = int(input('Choose region : '))
mx = -1
ans = ''
date = ''
for i in data:
    #print(i['rainfall'])
    if int(i['regcode']) == region:
        if i['rainfall'] > mx:
            mx = i['rainfall']
            ans = i['location']
            date = i['date']
print(f'- Max rainfall: {mx} mm.')
print(f'- Date: {date}')
print(f'- Location: {ans}')


