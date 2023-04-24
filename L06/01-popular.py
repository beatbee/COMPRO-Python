n = int(input("Input number of words: "))
D,cnt = {},{}
for i in range(n):
    word = input()
    D[word] = word[0]
for i in D.values():
    if i in cnt: cnt[i]+=1
    else: cnt[i] = 1
for i,j in cnt.items():
    if j == max(cnt.values()):
        ans = i
        print(f'The popular character is {ans}.')
ch,lst = 0,[]
for i,j in D.items():
    if j == ans:
        ch+=1
        lst.append(i)
print(f'The character is used in {ch} words.')
for i in lst: print(i)
"""
test case:
Input number of words: 5
deliver
throw on
double
mirror
zealous
The popular character is d.
The character is used in 2 words.
deliver
double
"""

