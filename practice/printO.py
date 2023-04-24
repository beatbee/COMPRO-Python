n = int(input())
s = input()
for i in range(n):
    print(" "*(n-i-1),end="")
    print(s*(2*i+1),end="")
    print()