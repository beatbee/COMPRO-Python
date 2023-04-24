s = int(input('Enter your score : '))
while s <0  or s>100:
    ans = int(input('Error score... Enter your score again : '))
    s = ans
if s >= 0 and s<=49:
    print('Grade F')
elif s<=59:
    print('Grade D')
elif s<=69:
    print('Grade C')
elif s<=79:
    print('Grade B')
else:
    print('Grade A')