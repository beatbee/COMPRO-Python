num,k = [int(x) for x in input("Grass: ").split()]
fench = [int(x) for x in input().split()]
ans = 0
for i in fench:
    if i >k:
        ans+=1
print(ans)