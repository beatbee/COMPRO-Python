"""
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
"""
import json
with open('todos.json','r') as fp:
    yes = fp.read()
s = json.loads(yes)
#print(type(s[0]))
user = {}
for i in s:
    if i['completed']:
        if i['userId'] not in user:
            user[i['userId']] = 1
        else:
            user[i['userId']] += 1
#print(user)
mx = max(user.values())
lst = []
for i,j in user.items():
    if j == mx:
        lst.append(i)
"""
for i in lst:
    print(i,end=' ')
#print(f'complete {mx}')
"""
"""
Question02
Now is your turn. Find the top three rank of users that are not completed the task.
"""
userno = {}
for i in s:
    if not i['completed']:
        if i['userId'] not in userno:
            userno[i['userId']] = 1
        else:
            userno[i['userId']] += 1
lstmax = []
ans = {}
ch = 0
for i in userno:
    lstmax.append(userno[i])
for i in (sorted(set(lstmax),reverse=True)):
    for j in userno:
        if userno[j] == i:
            if i not in ans:
                ans[i] = f'{j}'
            else:
                ans[i] += f' {j}'
for j in ans:
    if ch == 3:
        break
    else:
        print(f'users {ans[j]} not completed {j} TODOs')
        ch+=1

