n = int(input('How long have Buzz played ?: '))
ans = n//60
if n%60 > 20 :
    ans+=1
if ans >=2 and ans <4:
    k = int(900*ans*0.9)
    print(f'Total price is {k} baht.')
elif ans == 4:
    k = int(900*ans*0.8)
    print(f'Total price is {k} baht.')
elif ans>=5:
    k = round(900*ans*0.7)
    print(f'Total price is {k} baht.')
elif ans < 2:
    k = int(900*ans)
    print(f'Total price is {k} baht.')
elif ans == 0:
    k = int(900*ans)
    print(f'Total price is {k} baht.')