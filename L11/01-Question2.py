class City:
    def __init__(self, city, country, latitude, longitude, temperature):
        self.city = city
        self.country = country
        self.latitude = float(latitude)
        self.longitude = float(longitude)

file = input('Enter file name: ')
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
temp = []
for i in data1:
    city, country, latitude, longitude, temperature = i['city'],i['country'],i['latitude'],i['longitude'],i['temperature']
    x = City(city, country, latitude, longitude, temperature)
    temp.append(x.temperature)
temp.sort()
print(f'Minimum: {temp[0]:.2f}')
print(f'Maximum: {temp[-1]:.2f}')
print(f'Average temperature: {sum(temp)/len(temp):.4f}')




