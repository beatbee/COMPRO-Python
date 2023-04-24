a = int(input('a : '))
b = int(input('b : '))
gcd = 1
for i in range(2,max(a,b)+1):
    if a%i == 0  and b%i==0 :
        temp = i
        if temp > gcd:
            gcd = temp
lcd = gcd*(b/gcd)*(a/gcd)
print('GCD :',gcd)
print('LCM :',int(lcd))