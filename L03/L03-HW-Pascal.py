def Pascal(n):
    for j in range(n,0,-1):
        num = 1 
        for i in range(1,j+1):
            print(num, end = " ")
            num = int(num * (j-i) / i)
        print(" ")

n = int(input())
Pascal(n)

