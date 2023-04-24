d = int(input('d: '))
m = int(input('m: '))
y = int(input('y: '))
sum = 0
cnt = 0
if y%4!=0 or y%400 == 0:
    cnt = 0
else:
    cnt = 1
for i in range(1,m+1):
    if(i == 1 or i == 3 or i == 5 or i==7 or i == 8 or i==10 or i == 12):
        sum = d+cnt
        cnt +=31
    if(i == 2):
        sum = d+ cnt
        cnt +=28
    if(i == 4 or i == 6 or i == 9 or i == 11):
        sum = d+ cnt
        cnt+= 30
print(sum)

    