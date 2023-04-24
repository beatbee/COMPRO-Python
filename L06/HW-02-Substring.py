text = input("Text: ")
sub = input("Substring: ")
l = len(sub)
ans = ''
j = 0
while(j<len(text)):
    if text[j:j+l] ==  sub:
        #print('yay')
        ans += f'[{text[j:j+l]}]'
        j+=l 
    else:
        #print('no')
        ans+=f'{text[j]}'
        j+=1
if ans == text:
    print('Not found')
else:
    print(ans)
"""
Text: ababababababababab
Substring: aba
[aba]b[aba]b[aba]b[aba]bab
"""