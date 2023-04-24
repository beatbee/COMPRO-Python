a,b,c,d = map(int,input().split())
one,two,three,four = 0,0,0,0
#A
if(a>=b and a>=c and a>=d):
    four = a
    three = b
    if(b>=c and b>=d):
        three = b
        two = c
        one = d
        if(c>=d):
            two = c
            one = d
        else:
            two = d
            one = c
    elif(c>=b and c>=d):
        two = three
        three = c
        one = d
        if(b>=d):
            two = b
            one = d
        else:
            two = d
            one = b
    elif(d>=c and d>=b):
        two = three
        three = d
        one = c
        if(c>=b):
            two = c
            one = b
        else:
            two = b
            one = c
if(b>=c and b>=a and b>=d):
    four = b
    three = a
    if(a>=c and a>=d):
        three = a
        two = c
        one = d
        if(c>=d):
            two = c
            one = d
        else:
            two = d
            one = c
    elif(c>=a and c>=d):
        two = three
        three = c
        one = d
        if(a>=d):
            two = a
            one = d
        else:
            two = d
            one = a
    elif(d>=c and d>=a):
        two = three
        three = d
        one = c
        if(c>=a):
            two = c
            one = a
        else:
            two = a
            one = c
if(c>=b and c>=a and c>=d):
    four = c
    three = a
    if(a>=b and a>=d):
        three = a
        two = b
        one = d
        if(b>=d):
            two = b
            one = d
        else:
            two = d
            one = b
    elif(b>=a and b>=d):
        two = three
        three = b
        one = d
        if(a>=d):
            two = a
            one = d
        else:
            two = d
            one = a
    elif(d>=b and d>=a):
        two = three
        three = d
        one = b
        if(b>=a):
            two = b
            one = a
        else:
            two = a
            one = b
if(d>=c and d>=a and d>=b):
    four = d
    three = a
    if(a>=c and a>=b):
        three = a
        two = c
        one = b
        if(c>=b):
            two = c
            one = b
        else:
            two = b
            one = c
    elif(c>=a and c>=b):
        two = three
        three = c
        one = b
        if(a>=b):
            two = a
            one = b
        else:
            two = b
            one = a
    elif(b>=c and b>=a):
        two = three
        three = b
        one = c
        if(c>=a):
            two = c
            one = a
        else:
            two = a
            one = c

print(f'{one} {two} {three} {four}')

