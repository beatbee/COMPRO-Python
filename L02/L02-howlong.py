n = int(input('Input distance(kilometer): '))
ans = 0
h = 0
for i in range(n):
    ans+=10
    if(ans%60 == 0):
       ans+=10
if(ans%60 == 10):
    print(f'It takes {ans//60} hours and {0} minutes to reach the destination.') 
else:
    print(f'It takes {ans//60} hours and {ans%60} minutes to reach the destination.')

