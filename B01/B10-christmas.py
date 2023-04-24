level = int(input("How many levels? "))
s = int(input("Enter size of each bush: "))
for i in range(level):
    k = s-1
    for j in range(1,s+1):
        print(' '*k +'*'*(2*j-1),end='\n')
        k-=1