"""
class classes:
    def __init__(self,gender,race,level,lunch,test,math,reading,writing):
        self.gender = gender
        self.race = race
        self.level = level
        self.lunch = lunch
        self.test = test
        self.math = math
        self.reading = reading
        self.writing = writing
    def show_data(self):
        print(f'gender : {self.gender}')
        print(f'race/ethnicity : {self.race}')
        print(f'parental level of education : {self.level}')
        print(f'lunch : {self.lunch}')
        print(f'test preparation course : {self.test}')
        print(f'math score : {self.math}')
        print(f'reading score : {self.reading}')
        print(f'writing score : {self.writing}')
    def less_from_max_math_score(self):
        print(f'less than max : {mx - self.math}')
    def more_from_min_reading_score(self):
        print(f'more than min : {self.reading - mn}')
    def can_pass(self):
        if self.math + self.reading + self.writing > 240:
            print('pass')
        else:
            print('Can\'t pass')
    def print(self):
        print(f'math score : {self.math}, reading score : {self.reading}, writing score : {self.writing}')

file = input('Filename : ')
data1 = []
with open(file,'r') as fp:
    header = fp.readline().strip().split(',')
    for i in fp.read().strip().split('\n'):
        data = {}
        w = i.strip().split(',')
        w[0] = int(w[0])
        w[-1] = int(w[-1])
        w[-2] = int(w[-2])
        w[-3] = int(w[-3])
        for j in range(len(header)):
            data[header[j]] = w[j]
        data1.append(data)
n = int(input('Menu : '))
ID = int(input('ID : '))
for i in data1:
    if i['id'] == ID:
        gender,race,level,lunch,test,math,reading,writing = i['gender'],i['race/ethnicity'],i['parental level of education'],i['lunch'],i['test preparation course'],i['math score'],i['reading score'],i['writing score']
        id = classes(gender,race,level,lunch,test,math,reading,writing)
if n == 1:
    for i in data1:
        if i['id'] == ID:
            id.show_data()
elif n == 2:
    mx = -1
    for i in data1: 
        if i['math score'] > mx:
            mx = i['math score']
    id.less_from_max_math_score()
elif n == 3:
    mn = 2e9
    for i in data1: 
        if i['reading score'] < mn:
            mn = i['reading score']
    id.more_from_min_reading_score()
elif n == 4:
    id.can_pass()
elif n == 5:
    id.print()
"""
import csv
maxx = -1
minn = 1e9
def read_csv(filename):
    with open(filename) as f:
        global maxx , minn
        datas = csv.reader(f)
        data = [ i for i in datas]
        for i in range(1,len(data)) :
            maxx = max(maxx,int(data[i][6]))
            minn = min(minn,int(data[i][7]))
    return data
class Std:
    def __init__(self,id,gender,race,level,lunch,test,math,reading,writing):
        self.gender = gender
        self.race = race
        self.level = level
        self.lunch = lunch
        self.test = test
        self.math = math
        self.reading = reading
        self.writing = writing
        self.id = id
    def show_data(self):
        print(f'gender : {self.gender}')
        print(f'race/ethnicity : {self.race}')
        print(f'parental level of education : {self.level}')
        print(f'lunch : {self.lunch}')
        print(f'test preparation course : {self.test}')
        print(f'math score : {self.math}')
        print(f'reading score : {self.reading}')
        print(f'writing score : {self.writing}')
    def less_from_max_math_score(self):
        print(f'less than max : {maxx - int(self.math)}')
    def more_from_min_reading_score(self):
        print(f'more than min : {int(self.reading) - minn}')
    def can_pass(self):
        if int(self.math) + int(self.reading) + int(self.writing) > 240:
            print('pass')
        else:
            print('Can\'t pass')
    def __str__(self):
        return 'math score : ' + self.math + ', reading score : ' + self.reading +  ', writing score : ' + self.writing


filename = input("Filename : ")
datas = read_csv(filename)
classes = list()
for i in range(1,len(datas)) :
    id,gender,race,level,lunch,test,math,reading,writing = datas[i][0],datas[i][1],datas[i][2],datas[i][3],datas[i][4],datas[i][5],datas[i][6],datas[i][7],datas[i][8]
    data = Std(id,gender,race,level,lunch,test,math,reading,writing)
    classes.append(data)


menu = int(input("Menu : "))
id = input("ID : ")
for i in classes :
    if i.id == id :
        if menu == 1 : # show data
            i.show_data()
        elif menu == 2 : # less_from_max_math_score
            i.less_from_max_math_score()
        elif menu == 3 : # more_from_min_reading_score
            i.more_from_min_reading_score()
        elif menu == 4: # can_pass
            i.can_pass()
        elif menu == 5: # print
            print(i)
        break






#StudentsPerformance.csv