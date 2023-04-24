import json
file = input('Filename : ')
with open(file,'r') as fp:
    data = fp.read()
    data = json.loads(data)
n = int(input('Menu : '))
if n== 1:
    print(len(data))
elif n == 2:
    f= int(input('From : '))
    t = int(input('To : '))
    start = input('Start with Char : ')
    for i in range(f,t+1):
        if data[i]['title'][0].upper() == start :
            x = data[i]['title']
            print(f'{i} : {x}')
elif n == 3:
    ch = 0
    mx = -1
    mx1 = -1
    ans = []
    ans1 = []
    f= int(input('From : '))
    t = int(input('To : '))
    type = input('Type : ')
    for i in range(f,t+1):
        if data[i]['type'] == type:
            ch+=1
            if data[i]['mal_score'] > mx1 :
                mx1 = data[i]['mal_score']
            if data[i]['mal_favorites'] > mx :
                mx = data[i]['mal_favorites']
    for i in range(f,t+1):
        if data[i]['mal_score'] == mx1:
            ans.append(data[i]['title'])
        if data[i]['mal_favorites'] == mx :
            ans1.append(data[i]['title'])
    print(f'{type} : {ch}')
    print(f'Most scores : {ans[0]}')
    print(f'Most favorites : {ans1[0]}')
elif n == 4:
    f= int(input('From : '))
    t = int(input('To : '))
    source = input('Source : ')
    status = input('Status : ')
    score = float(input('Mul score : '))
    for i in range(f,t+1):
        if data[i]['source'] == source:
            if data[i]['status'] == status:
                if data[i]['mal_score'] > score:
                    x = data[i]['title']
                    print(f'{i} : {x}')
elif n == 5:
    ch = 0
    f= int(input('From : '))
    t = int(input('To : '))
    ss = input('Season : ')
    for i in range(f,t+1):
        if data[i]['premiered'] != None and data[i]['premiered'] != 'NULL':
            if data[i]['premiered'].split()[0] == ss:
                ch+=1
    print(f'{ss} : {ch}')
elif n == 6:
    ch = 0
    f= int(input('From : '))
    t = int(input('To : '))
    for i in range(f,t+1):
        if data[i]['aired_start'] != None and data[i]['aired_start'] != 'NULL' and data[i]['aired_end'] != None and data[i]['aired_end'] != 'NULL':
            x = data[i]['aired_end'].split('-')
            y = data[i]['aired_start'].split('-')
            if x[0] == y[0]:
                ch+=1
    print(f'Find : {ch}')
elif n == 7:
    tt = input('Title : ')
    for i in range(len(data)):
        if data[i]['title'] == tt:
            print(data[i]['mal_rating'])
elif n== 8:
    mx = -1
    ans = ''
    D = {}
    DD = {}
    f= int(input('From : '))
    t = int(input('To : '))
    for i in range(f,t+1):
        if len(data[i]['synopsis'].split()) >= mx:
            mx = len(data[i]['synopsis'].split())
            x = data[i]['title']
            D[i] = x
            DD[i] = mx
    for i,j in D.items():
        if DD[i] == mx:
            print(f'{i} : {j}')




#MyAnimeList_Anime_2021_05_16.json
