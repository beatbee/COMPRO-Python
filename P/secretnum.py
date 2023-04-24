import random
s = random.randint(1,20)
for i in range(1,7):
    g = int(input('Take a guess:' ))
    if g < s:
        print("low")
    elif g>s:
        print("high")
    else:
        break
if g == s:
    print('gg')
else:
    print('hi'+str(s))