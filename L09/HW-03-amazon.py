import json
file = input('file name: ')
n = int(input('input: '))
with open(file,'r') as fp:
    yes = fp.read().split('\n')
s= []
for i in range(len(yes)):
    ss = json.loads(yes[i])
    s.append(ss)
if n == 1:
    print(len(s))
elif n == 2:
    review = []
    for i in s:
        if i['reviewerID'] not in review:
            review.append(i['reviewerID'])
    print(len(review))
elif n == 3:
    goods = []
    for i in s:
        if i['productID'] not in goods:
            goods.append(i['productID'])
    print(len(goods))
elif n == 4:
    pro = []
    for i in s:
        w = i['category'].strip().split('>')
        if w[0].strip() not in pro:
            pro.append(w[0].strip())
    print(len(pro))
elif n == 5:
    pro = []
    for i in s:
        w = i['category'].strip().split(' > ')
        if w[1].strip() not in pro:
            pro.append(w[1].strip())
    print(len(pro))
elif n == 6:
    ans = ''
    mx = -1
    user = {}
    for i in s:
        if i['reviewerID'] not in user:
            user[i['reviewerID']] = 1
        else:
            user[i['reviewerID']] += 1
    for i in user:
        if user[i] > mx:
            mx = user[i]
            ans = i
    print(ans)
elif n == 7:
    review = {}
    total = {}
    pro = {}
    ans = ''
    mx = -1
    for i in s:
        if i['productName'] not in review:
            review[i['productName']] = i['overall']
            total[i['productName']] = 1
        else:
            review[i['productName']] += i['overall']
            total[i['productName']] += 1
    for i in s:
        pro[i['productName']] = review[i['productName']]/total[i['productName']]
    for i in pro:
        if pro[i] == 5.0:
            if total[i] > mx:
                mx = total[i]
                ans = i
    print(ans)
elif n == 8:
    user = {}
    pro = {}
    mx = -1
    ans = ''
    for i in s:
        if i['productName'] not in user:
            user[i['productName']] = len(i['reviewText'].split())
            pro[i['productName']] = 1
        else:
            user[i['productName']] += len(i['reviewText'].split())
            pro[i['productName']] += 1
    for i in s:
        if user[i['productName']]/pro[i['productName']] > mx:
            ans = i['productName']
            mx = user[i['productName']]/pro[i['productName']]
    print(ans)
#amazon1 2.json