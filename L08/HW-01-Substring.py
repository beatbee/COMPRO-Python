text = input("Text: ")
sub = input("Substring: ")
l = len(sub)
ans = ''
j = 0
while(j<len(text)):
    if text[j:j+l] ==  sub:
        ans += f'[{text[j:j+l]}]'
        j+=l 
    else:
        ans+=f'{text[j]}'
        j+=1
if ans == text:
    ans = ''
    j= 0
    while(j<len(text)):
        if text[j] == sub[0]:
            if len(text)-j < l:
                ans+=f'{text[j:j+(len(text)-j)]}'
                break             
            ch = 0
            k = j
            for z in range(l):
                if text[k] == sub[z]:
                    ch+=1
                k+=1     
            if ch == l-1:
                x = list(text[j:j+l])
                for i in range(l):
                    if x[i] != sub[i]:
                        x[i] = '?'
                        y = ''.join(x)
                        ans += f'[{y}]'
                        x = list(text[j:j+l])
                j+=l
            else:
                ans+=f'{text[j]}'
                j+=1            
        else:
            ans+=f'{text[j]}'
            j+=1
    print(ans)
else:
    print(ans)
"""
Text: acabababababcbabab
Substring: aba
ac[aba]b[aba]babcb[aba]b
Example 2
Text: acababababaccbabab
Substring: abc
ac[ab?]b[ab?]b[a?c]b[ab?]b
Example 3
Text: AAAGTGTGTCTGAC
Substring: GTAT
AAA[GT?T][GT?T]GAC
"""