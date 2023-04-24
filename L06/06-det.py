one = [int(x) for x in input("Row 1 :").split()]
two = [int(x) for x in input("Row 2 :").split()]
three = [int(x) for x in input("Row 3 :").split()]
one.extend(one[:2])
two.extend(two[:2])
three.extend(three[:2])
A = []
A.append(one)
A.append(two)
A.append(three)
tot1 = 0
for i in range(3):
    ch = 0
    ans = 1
    for j in range(3):
        ans*=A[ch][i+ch]
        ch+=1
    tot1 +=ans
tot2 = 0
for i in range(3):
    ch = 2
    ans = 1
    for j in range(3):
        ans*=A[ch][i+j]
        ch-=1
    tot2 +=ans
print(tot1-tot2)
"""
Row 1 : 1 5 3
Row 2 : 2 4 7
Row 3 : 4 6 2
74
"""
