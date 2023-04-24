n = int(input("N = "))
m = int(input("M = "))
lst = []
mn = 2e9
for i in range(n):
    cost = int(input(f"cost of day {i+1} = "))
    lst.append(cost)
for i in range(n-m+1):
    ans = 0
    for j in range(m):
        ans+=lst[i+j]
    if ans<mn:
        mn = ans
print(f'Min cost of {m} days = {mn}')
"""
N = 6
M = 5
cost of day 1 = 4
cost of day 2 = 2
cost of day 3 = 2
cost of day 4 = 3
cost of day 5 = 4
cost of day 6 = 2
Min cost of 5 days = 13
"""
