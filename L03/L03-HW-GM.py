def even_check(num):
    if num%2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
def prime_check(num):
    if num == 1 or num == 0:
        print("The number is not prime")
    else:
        ans = 0
        for i in range(2,num):
            if  num%i == 0:
                ans+=1
        if  ans > 0 and num!=2:
            print("The number is not prime")
        elif(num == 2):
            print("The number is prime")
        else:
            print("The number is prime")

num = int(input("Number : "))
even_check(num)
prime_check(num)