lucky = input("Enter lucky number : ")
candidate = int(input("Enter amount of candidates : "))
mx = -1
ans = 0
for i in range(candidate):
    ch = 0
    num = input(f"Enter ID card number {i+1}: ")
    for i in num:
        if i == lucky:
            ch+=1
    if ch>mx:
        mx = ch
        ans = num
    elif ch == mx and ch!= 0 and mx!=0:
        for i in range(len(ans)-1):
            if int(ans[i])<int(num[i]):
                ans = num
                break
            elif int(ans[i])>int(num[i]):
                ans = ans
                break
            else:
                continue        
print(f"Winner: {ans}")
    

