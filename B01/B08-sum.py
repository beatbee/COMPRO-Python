sumplus = 0
summinus = 0
while(True):
    n = float(input("Enter a number (or zero to exit): "))
    if n == 0:
        break
    if n >0 :
        sumplus+=n
    else:
        summinus+=n
print(f'The sum of all positive numbers is {sumplus:.2f}')
print(f'The sum of all negative numbers is {summinus:.2f}')