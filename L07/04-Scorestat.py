lst = []
while True:
    n = input('Input student score (or just ENTER to end): ')
    if n == '':
        break
    else:
        n=int(n)
        lst.append(n)
c = 1
for i in lst:
    print(f'Student #{c} score: {i}')
    c+=1
print(f'Average score is {sum(lst)/len(lst):.2f}')
print(f'Minimum score is {min(lst)}')
print(f'Maximum score is {max(lst)}')
    
