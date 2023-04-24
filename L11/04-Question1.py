class Country:
    def __init__(self, country, population, EU,coastline):
        self.country = country
        self.population = float(population)
        self.EU = EU
        self.coastline = coastline

file = input('Enter File name: ')
data1 = []
with open(file,'r') as fp:
    header = fp.readline().strip().split(',')
    for i in fp.read().strip().split('\n'):
        data = {}
        w = i.strip().split(',')
        for j in range(len(header)):
            data[header[j]] = w[j]
        data1.append(data)
lst = []
for i in data1:
    country, population, EU,coastline = i['country'],i['population'],i['EU'],i['coastline']
    x = Country(country, population, EU,coastline)
    if x.EU == 'yes' and x.coastline == 'no':
        print(x.country,x.population)