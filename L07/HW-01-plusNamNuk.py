n = int(input("N : "))
D = {}
for i in range(n):
    word = input().split()
    D[word[0]] = int(word[1])
text = input().split('+')
text1 = []
for i in text:
    if ' 'in i:
        x = list(i)
        for j in x:
            if ' ' in j:
                x.remove(' ')
        new = ''.join(x)
        text1.append(new)
    else:
        text1.append(i)
ans = 0
for i in range(len(text1)):
    if text1[i] in D:
        ans+=D[text1[i]]
print(ans)