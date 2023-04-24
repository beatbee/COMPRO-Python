def displaysub():
    s = ''
    lst = []
    ch = 1
    for i in range(len(subList)):
        s += f'[{ch}] {subList[i]}'
        lst.append(s)
        s = ''
        ch +=1
        if ch%2 == 1:
            print(f'{lst[0]:<20}{lst[1]}')
            lst = []
def calGPA(total):
    stu = {}
    tt = 0
    gpa = 0
    for i,j in total.items():
        tt += subDic[i]*grade[j]
        gpa += subDic[i]
    tt/=gpa
    return tt

def getsub(name):
    total = {}
    while(True):
        displaysub()
        sub = int(input('Enroll your subject(1...8 or 0 exit): '))
        if sub<9 and sub>0:
            g = input('Your grade: ')
            total[subList[sub-1]] = g.upper()
        elif sub == 0:
            check = input('You want to exit?(y/n): ')
            if check == 'y':
                break
            else:
                continue
        print(name,total)
    return total
def getname():
    student = {}
    while(True):
        name = input('Name pls: ')
        if name == '':
            print('Thankyou')
            break
        x = getsub(name)
        student[name] = x
        y = calGPA(x)    
        print(student)
        print(y)
    return student
def printgrade(student):
    s = ''
    for i,j in student.items():
        s+= f'{i}: '
        for p,q in j.items():
            s+= f'{p} {subDic[p]}c,{q} '
        s+= f'GPA : {calGPA(j)}'
        print(s)
        s = ''
    print('End')


subDic = {'Physic I': 3, 'Lab Physic I': 1, 'Math I': 3, 'Com Programming': 3, 'Thai Lang Com': 3, 'Art of Living': 3, 'Land of Smile': 3, 'Intro Japanese': 3}
subList = ['Physic I', 'Lab Physic I', 'Math I', 'Com Programming', 'Thai Lang Com', 'Art of Living', 'Land of Smile', 'Intro Japanese']
grade = {'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}
x = getname()
printgrade(x)
"""
def testprint():
    print({'Kun Toto': {'Physic I': 'A', 'Lab Physic I': 'C+', 'Thai Lang Com': 'B+', 'Land of Smile': 'D', 'Intro Japanese': 'B+'}, 'Somchai Rukdee': {'Lab Physic I': 'B+', 'Physic I': 'B', 'Math I': 'C', 'Com Programming': 'D', 'Thai Lang Com': 'F', 'Art of Living': 'A', 'Land of Smile': 'A'}})
    print('name : Kun Toto')
    print({'Physic I': 'A', 'Lab Physic I': 'C+', 'Thai Lang Com': 'B+', 'Land of Smile': 'D', 'Intro Japanese': 'B+'})
    print('grade : 3.5')
def printmenu():
    line = []
    for i in range(len(subList)):
        s = ''
        s+=f'[{i+1}] '
        s+=subList[i]
        s+=f' {subDic[subList[i]]}credits'
        line.append(s)
        if i%2 == 1:
            print(f'{line[0]:<30} {line[1]}')
            line = []
    print(f'[9] exit')
def calGPA(enrollsub):
    credits = 0
    g = 0
    for i ,j in enrollsub.items():
        credits+=subDic[i]
        g += grade[j] * subDic[i]
    total = g/credits
    return total

def getname():
    lststu = {}
    while True:
        name = input("Enter your name or Enter to exit : ")
        if name == '':
            break
        if name in lststu:
            print('You already enroll')
        else:
            enrollsub = {}
            while True:
                printmenu()
                n = int(input("Choose Subject : "))
                if n == 9:
                    break
                if n not in range(1,9):
                    print('only 1-9 is valid')
                else:
                    if subList[n-1] in enrollsub:
                        print('You already enroll this subject')
                    else:
                        print(f'{subList[n-1]}')
                        while True:
                            g = input(f"Your {subList[n-1]} grade : ").upper()
                            if g not in grade:
                                print("Only A,B+,B,...,F is valid")
                            else:
                                enrollsub[subList[n-1]] = g
                                print(enrollsub)
                                break
            lststu[name] = enrollsub
    return lststu
def printgrade(total):
    for i,j in total.items():
        print('name : ',i)
        print(j)
        x = calGPA(j)
        print(f'grade : {x}')

            
grade = {'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}
subDic = {'Physic I': 3, 'Lab Physic I': 1, 'Math I': 3, 'Com Programming': 3, 'Thai Lang Com': 3, 'Art of Living': 3, 'Land of Smile': 3, 'Intro Japanese': 3}
subList = ['Physic I', 'Lab Physic I', 'Math I', 'Com Programming', 'Thai Lang Com', 'Art of Living', 'Land of Smile', 'Intro Japanese']
x = getname()
printgrade(x)
"""