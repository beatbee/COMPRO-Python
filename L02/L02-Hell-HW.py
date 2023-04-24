a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
while a+b+c != 1:
    if a>=b and b>=c:
        a-=1
        b-=1
        c+=1
    elif a>=c and c>=b:
        a-=1
        c-=1
        b+=1
    elif b>=c and c>=a:
        b-=1
        c-=1
        a+=1
    elif b>=a and a>=c:
        b-=1
        a-=1
        c+=1
    elif c>=a and a>=b:
        c-=1
        a-=1
        b+=1
    elif c>=b and b>=a:
        c-=1
        b-=1
        a+=1
if a== 1 : print('A')
if b== 1 : print('B')
if c== 1 : print('C')
