class MyMath:
    def is_even(self,n):
        if n % 2 == 0:
            return True
        else:
            return False
    def fac(self,n):
            ans = n
            ans1 = 1
            while ans >= 1:
                ans1*=ans
                ans-=1
            return ans1
    def is_prime(self,n):
        ch = 0
        if n == 1 or n == 0:
            return False
        else:
            ans = 0
            for i in range(2,n):
                if  n%i == 0:
                    ans+=1
            if  ans > 0 and n!=2:
                return False         
            elif(n == 2):
                return True
            else:
                return True
    def divide_by(self,n,k):
        if n % k == 0:
            return True
        else:
            return False
    def ten_to_bi(self,n):
        ans = ''
        ch = n
        while ch>=1:
            ans += f'{ch%2}'
            ch//=2
        ans = list(ans)
        ans = ''.join(ans[::-1])
        return ans
    def ten_to_oct(self,n):
        ans = ''
        ch = n
        while ch>=1:
            ans += f'{ch%8}'
            ch//=8
        ans = list(ans)
        ans = ''.join(ans[::-1])
        return ans
    def ten_to_sixteen(self,n):
        ans = ''
        ch = n
        while ch>=1:
            if ch%16 < 10 :
                ans += f'{ch%16}'
                ch//=16
            else:
                if ch%16 == 10 : ans+='A'
                elif ch%16 == 11 : ans+='B'
                elif ch%16 == 12 : ans+='C'
                elif ch%16 == 13 : ans+='D'
                elif ch%16 == 14 : ans+='E'
                elif ch%16 == 15 : ans+='F'
                ch//=16   
        ans = list(ans)
        ans = ''.join(ans[::-1])
        return ans
    def int_to_roman(self,n):
        a = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        ans = ''
        ch = n
        j = 0
        while ch > 0:
            for i in range(ch//a[j]):
                ans += roman[j]
                ch-=a[j]
            j+=1
        return ans
    ans = 3
    j = 2
    ch = 0
    for i in range(50):
        if ch == 0:
            ans+=(4/(j*(j+1)*(j+2)))
            ch = 1
        else:
            ans+=(-4/(j*(j+1)*(j+2)))
            ch = 0
        j+=2
    pi = ans
my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))
if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num,k)):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')
"""
n = int(input('Please Enter Number : '))
d = int(input('Divide by? : '))
i = Cal(n,d)
print(f'{i.even()}')
print(i.fac())
print(i.prime())
print(i.divide())
print(i.two())
print(i.eight())
print(i.six())
print(i.roman())
print(i.calPi())
"""