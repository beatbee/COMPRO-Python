class City:
    def __init__(self, city, country, latitude, longitude, temperature):
        self.city = city
        self.country = country
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.temperature = float(temperature)
file = input('Enter file name: ')
data1 = []
c = []
with open(file,'r') as fp:
    header = fp.readline().strip().split(',')
    for i in fp.read().strip().split('\n'):
        data = {}
        w = i.strip().split(',')
        for j in range(len(header)):
            data[header[j]] = w[j]
        city, country, latitude, longitude, temperature = data['city'],data['country'],data['latitude'],data['longitude'],data['temperature']
        x = City(city, country, latitude, longitude, temperature)
        data1.append(x)
        if x.country not in c:
            c.append(x.country)
lst = []
for i in c:
    t = 0
    cnt = 0
    for j in data1:
        if j.country == i:
            t+=j.temperature
            cnt+=1
    print(f'{i} {t/cnt:.2f}')

