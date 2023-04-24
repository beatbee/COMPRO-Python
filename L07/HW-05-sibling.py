n = int(input())
check = {}
for i in range(n):
    text = [x for x in input().split()]
    if text[2] == 'mother' or text[2] == 'father':
        if text[0] in check:
            check[text[0]] += f'{text[4]}'
        else:
            check[text[0]] = f'{text[4]}'
word = input().split()
cnt = 0
for i,j in check.items():
    if word[1] in j and word[3] in j:
        print('Yes')
        cnt = 1
if cnt == 0:
    print('No')

