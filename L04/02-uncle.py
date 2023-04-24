n = int(input("N = "))
lst = []*n
mn = 10000000
ans = 0
for i in range(n):
    cost = int(input(f"cost of day {i+1} = "))
    lst.append(cost)
for i in range(len(lst)-2):
    ans = lst[i] + lst[i+1] + lst[i+2]
    if ans<mn:
        mn = ans
print(f"Min cost of 3 days = {mn}")

        
