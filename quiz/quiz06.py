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

def q01(myCity, myCountry):
    for i in myCountry:
        cnt = 0
        tem = 0
        if i.EU == 'yes' and i.coastline == 'no':
            for j in myCity:
                if j.country == i.country:
                    tem+=j.temp
                    cnt+=1
            if cnt == 0:
                continue
            print(f'{i.country}: {tem/cnt:.2f}')

def q02(myCity, myCountry):
    ans1 = ''
    ans2 = ''
    mx = -1
    mn = 1000000
    for i in myCountry:
        cnt = 0
        tem = 0
        if i.EU == 'no':
            for j in myCity:
                if j.country == i.country:
                    tem+=j.temp
                    cnt+=1
            if cnt == 0:
                continue
            if tem/cnt > mx:
                mx = tem/cnt
                ans1 = i.country
            if tem/cnt < mn:
                mn = tem/cnt
                ans2 = i.country
    print(f'The highest average city temperature: {ans1} ({mx:.2f})')
    print(f'The lowest average city temperature: {ans2} ({mn:.2f})')

### main begins here
myCity = readCity()
myCountry = readCountry()
q01(myCity,myCountry)
q02(myCity,myCountry)