n = int(input('How many day : '))
ans1 = 0
h = 0.95
for i in range(1,n+1):
    x = float(input(f'Input price in day {i} : '))
    ans1 += x*h
    h-=0.01
print('Summary price = ''%.2f'%ans1)
