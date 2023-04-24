a,b,c,d = map(int,input().split())
one,two,three,four = 0,0,0,0
four = d
if(c>four):
    three = four
    four = c
else:
    three = c
if(b>four):
    two = three
    three = four
    four = b
elif(b>three):
    two = three
    three = b
else:
    two = b
if(a>four):
    one = two
    two = three
    three = four
    four = a
elif(a>three):
    one = two
    two = three
    three =a
elif(a>two):
    one = two
    two = a
else:
    one = a
print(f'{one} {two} {three} {four}')






