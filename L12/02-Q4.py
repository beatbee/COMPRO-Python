class City:
  nbCity = 0
  def __init__(s,city,country,lat,long,temp):
    s.city = city; s.country = country; s.lat = lat
    s.long = long; s.temp = temp; City.nbCity += 1
class Country:
  nbCountry = 0
  def __init__(self,country,population,EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry +=1

def readCity():
  myCity = []
  with open('Cities.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity

def test_readCity(myCity):
  for c in myCity:
    print(c.city,c.country,c.lat,c.long,c.temp)

def readCountry():
  myCountry = []
  with open('Countries.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      country,population,EU,coastline = cc[0],float(cc[1]),cc[2],cc[3]
      myCountry.append(Country(country,population,EU,coastline))
  return myCountry

city = input('Enter city file: ')
country = input('Enter country file: ')
myCity = readCity()
myCountry = readCountry()
print('Average temperature of countries having coastline, but not in EU:')
for i in myCountry:
    cnt = 0
    tem = 0
    if i.EU == 'no' and i.coastline == 'yes':
        for j in myCity:
            if j.country == i.country:
                tem+=j.temp
                cnt+=1
        if cnt == 0:
            continue
        print(f'{i.country} {tem/cnt:.2f}')