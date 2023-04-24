lst = []
while True:
    n = input('Input student score (or just ENTER to end): ')
    if n == '':
        break
    else:
        x = int(n)
        lst.append(x)
ave = sum(lst)/len(lst)
sumstd = 0
for i in lst:
    sumstd += (i-ave)**2
std = (sumstd/(len(lst)-1))**0.5
print(f'Average score is {ave:.2f}')
print(f'Standard deviation is {std:.2f}')
j = 1
for i in lst:
    if i >= ave+1.5*std:
        print(f'Student #{j} score: {i} grade: A')
    elif i<ave+1.5*std and i>= ave+std:
        print(f'Student #{j} score: {i} grade: B+')
    elif i<ave+std and i >= ave+0.5*std:
        print(f'Student #{j} score: {i} grade: B')
    elif i<ave+0.5*std and i >=ave:
        print(f'Student #{j} score: {i} grade: C+')
    elif i< ave and i>=ave-0.5*std:
        print(f'Student #{j} score: {i} grade: C')
    elif i<ave-0.5*std and i>=ave-std:
        print(f'Student #{j} score: {i} grade: D+')
    elif i< ave-std and i >=ave-1.5*std:
        print(f'Student #{j} score: {i} grade: D')
    elif i<ave-1.5*std:
        print(f'Student #{j} score: {i} grade: F')
    j+=1



