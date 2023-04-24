s = ''
with open('score.csv', 'r') as fp:
    s = fp.read()
totalst = 0
mx = -1
mn = 1000
grade = {'A' : 0,'B+' : 0,'B' : 0,'C+' : 0,'C' : 0,'D+' : 0,'D' : 0,'F' : 0}
totalscore = 0
for i in s.split('\n'):
    if i!='' and i != 'Test name,Test taken on,Total questions,Items attempted,Items not attempted,Answered correct,Answered wrong,Score,Percentage,Grade':
        w = i.split(',')
        if w[8]!= '0':
            totalst+=1
        if float(w[7]) > mx:
            mx = float(w[7])
        if float(w[7]) < mn and float(w[7]) != 0:
            mn = float(w[7])
        if float(w[8]) > 85:
            grade['A'] +=1
        elif float(w[8]) >79:
            grade['B+'] +=1
        elif float(w[8]) >73:
            grade['B'] +=1
        elif float(w[8]) > 67:
            grade['C+']+=1
        elif float(w[8]) >60:
            grade['C']+=1
        elif float(w[8]) > 50:
            grade['D+']+=1
        elif float(w[8]) > 40:
            grade['D']+=1
        elif float(w[8]) >0:
            grade['F']+=1
        totalscore += float(w[7])
ave = totalscore/totalst
tstd = 0
for i in s.split('\n'):
    if i!='' and i != 'Test name,Test taken on,Total questions,Items attempted,Items not attempted,Answered correct,Answered wrong,Score,Percentage,Grade':
        w = i.split(',')
        if w[7] != '0':
            tstd += (float(w[7]) - ave)**2
std = (tstd/totalst)**0.5
print(totalst)
print(f'{int(mx)} {ave:.2f} {std:.2f} {int(mn)}')
for i,j in grade.items():
    print(f'{i}: {j}')
    