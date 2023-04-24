text = [x for x in input("Text: ").split()]
ans = 0
chain = 1
mx = 0
cnt = 1
for i in range(len(text)-1):
    ans = 0
    for j in range(len(text[i])):
        if text[i][j] != text[i+1][j]:
            ans+=1
        #print(text[i][j],text[i+1][j])
    if ans > 2:
        chain+=1
        cnt = 1
    if ans<=2:
        cnt +=1
    if cnt>mx:
        mx = cnt
    #print(ans,chain,cnt)
print(f'{chain} Chain(s). Maximum length is {mx} word(s).')