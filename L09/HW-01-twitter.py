import json
file = input('File name: ')
n = int(input('input: '))
with open(file,'r') as fp:
    yes = fp.read()
s = json.loads(yes)
if n == 1:
    print(len(s))
elif n == 2:
    user = []
    for i in s:
        if i['author'] not in user:
            user.append(i['author'])
        else:
            pass
    print(len(user))
elif n == 3:
    user = {}
    lst = []
    for i in s:
        if i['author'] not in user:
            user[i['author']] = 1
        else:
            user[i['author']] += 1
    for i in user.values():
        lst.append(i)
    x = sorted(lst,reverse=True)
    for k,l in user.items():
        if l == x[0]:
            print(k)
elif n == 4:
    topic = []
    for i in s:
        if i['topic'] not in topic:
            topic.append(i['topic'])
        else:
            pass
    print(len(topic))
elif n == 5:
    cnt = 0
    for i in s:
        if i['topic_priority'] == 'ALERT':
            cnt+=1
    print(cnt)
elif n == 6:
    cnt = 0
    for i in s:
        if i['topic_priority'] == 'UNIMPORTANT':
            cnt+=1
    print(cnt)
elif n == 7:
    ch = 0
    for i in s:
        if i['language'] != 'EN':
            print('True')
            ch = 1
            break
    if ch == 0:
        print('False')
elif n == 8:
    mx = -1
    for i in s:
        if len(i['text'].split()) > mx:
            mx = len(i['text'].split())
    print(mx)
    


        



