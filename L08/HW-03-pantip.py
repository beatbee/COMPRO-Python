file = input('File name: ')
D = {}
userid = {}
with open(file,'r') as fp:
    header = fp.readline()
    x = header.strip().split(',')
    s = fp.read()
    for i in range(len(x)):
        D[x[i]] = []
    for i in s.strip().split('\n'):
        w = i.strip().split(',')
        userid[w[-1]] = []
        for k in range(len(w)-1):
            D[x[k]].append(int(w[k]))
            userid[w[-1]].append(int(w[k]))
n = int(input('enter number: '))
if n == 1:
    print(len(s.split('\n')))
elif n ==2:
    mx = -1
    ans = ''
    for i in D:
        if sum(D[i]) > mx:
            mx = sum(D[i])
            ans = i
    print(ans)
elif n == 3:
    m1 = -1
    m2 = -1
    for i in D['blueplanet']:
        if i > m1:
            m3 = m2
            m2 = m1
            m1 = i
        elif i > m2:
            m3 = m2
            m2 = i
    print(m1,m2,m3)
    x = sorted(D['blueplanet'],reverse=True)
    print(x[0],x[1],x[2])
elif n == 4:
    mx = -1
    a = ''
    for i in userid:
        ans = sum(userid[i])
        if  ans>mx:
            mx = ans
            a = i
    print(a,mx)
elif n == 5:
    mx = -1
    a = ''
    for i in userid:
        if i!= '' and userid[i][0] >mx:
            mx = userid[i][0]
            a = i
    print(a,mx)
elif n == 6:
    cnt = 0
    for i in D['korea']:
        if i > 500:
            cnt+=1
    print(cnt)
elif n == 7:
    cnt = 0
    for i in range(len(userid)):
        if i!='' and D['siam'][i] > D['food'][i]:
            cnt+=1
    print(cnt)
elif n == 8:
    mx = -1
    a = ''
    cnt = 0
    for i in D:
        if i == 'rajdumnern':
            break
        cnt+=1
    for i in userid:
        if i!='' and userid[i][cnt]/sum(userid[i]) >mx :
            mx = userid[i][cnt]/sum(userid[i])
            a = i
    print(a)
elif n == 9:
    nine = {}
    cnt = 0
    for i in userid:
        m1 = -1
        for j in range(len(D)-1):
            if i!='' and userid[i][j] > m1:
                m2 = m1
                m1 = userid[i][j]
            elif i!='' and userid[i][j] > m2:
                m2 = userid[i][j]
        if sum(userid[i]) != 0:
            nine[i] = (m1+m2)/sum(userid[i]) 
        if i!='' and nine[i] > 0.7:
            cnt+=1
    print(cnt)   
elif n == 10:
    cnt = 0
    for i in range(len(userid)-1):
        if D['pantip'][i] == 0:
            cnt+=1
    print(cnt)

"""
pantip-read-20181015-20181222.csv
1.ข้อมูลมีทั้งหมดกี่บรรทัด (รวมheader)
2.ห้องไหนที่มีจำนวนการกดอ่านมากที่สุด
3.ห้อง blueplanet มีการกดอ่านมากสุด3อันดับแรก เป็นจำนวนกี่ครั้ง
4.user ไหนมีจำนวนการอ่านรวมทุกห้องมากที่สุด จำนวนกี่ครั้ง
5.user ไหนอ่านห้อง tvshow มากที่สุด เป็นจำนวนกี่ครั้ง
6.ห้อง korea มี user ที่กดอ่านมากกว่า 500 กระทู้ทั้งหมดกี่คน
7.มี user ที่่อ่านห้อง siam มากกว่า food กี่คน
8.user ไหนมีสัดส่วนการอ่านในห้อง rajdumnern มากที่สุด
9.user ที่มีสัดส่วนการอ่านใน 2 ห้อง มากกว่า 70% มีทั้งหทดกี่คน
10.user ที่ไม่อ่านห้อง pantip มีทั้งหมดกี่คน
"""
"""
file = input('File name: ')
D = {}
userid = {}
with open(file,'r') as fp:
    header = fp.readline().split(',')
    for i in fp.readlines():
        user1 = {}
        if i.strip() != '':
            w = i.strip().split(',')
            for j in range(len(header)-1):
                if header[j] not in D:
                    D[header[j]] = [int(w[j])]
                else:
                    D[header[j]].append(int(w[j]))
                user1[header[j]] = int(w[j])
                w[j] = int(w[j])
            userid[w[-1]] = user1
    #print(user['pf4unt4gz1T3NV1j7f7y'])
n = int(input('N : '))
if n == 1:
    print(len(D['tvshow'])+1)
if n == 2:
    mx,ans = -1,''
    for i in D:
        if sum(D[i]) > mx:
            mx = sum(D[i])
            ans = i
    print(ans)
elif n == 3:
    m1 = -1
    m2 = -1
    for i in D['blueplanet']:
        if i > m1:
            m3 = m2
            m2 = m1
            m1 = i
        elif i > m2:
            m3 = m2
            m2 = i
    print(m1,m2,m3)
elif n == 4:
    mx = -1
    a = ''
    for i in userid:
        for j in D:
            ans = sum(userid[i][j])
            if  ans>mx:
                mx = ans
            a = i
    print(a,mx)
elif n == 5:
    mx = -1
    a = ''
    for i in userid:
        if i!= '' and userid[i][0] >mx:
            mx = userid[i][0]
            a = i
    print(a,mx)
elif n == 6:
    cnt = 0
    for i in D['korea']:
        if i > 500:
            cnt+=1
    print(cnt)
elif n == 7:
    cnt = 0
    for i in range(len(userid)-1):
        if i!='' and D['siam'][i] > D['food'][i]:
            cnt+=1
    print(cnt)
elif n == 8:
    mx = -1
    a = ''
    cnt = 0
    for i in D:
        if i == 'rajdumnern':
            break
        cnt+=1
    for i in userid:
        if i!='' and userid[i][cnt]/sum(userid[i]) >mx :
            mx = userid[i][cnt]/sum(userid[i])
            a = i
    print(a)
elif n == 9:
    nine = {}
    cnt = 0
    for i in userid:
        m1 = -1
        for j in range(len(D)-1):
            if i!='' and userid[i][j] > m1:
                m2 = m1
                m1 = userid[i][j]
            elif i!='' and userid[i][j] > m2:
                m2 = userid[i][j]
        if sum(userid[i]) != 0:
            nine[i] = (m1+m2)/sum(userid[i]) 
        if i!='' and nine[i] > 0.7:
            cnt+=1
    print(cnt)   
elif n == 10:
    cnt = 0
    for i in range(len(userid)-1):
        if D['pantip'][i] == 0:
            cnt+=1
    print(cnt)
"""