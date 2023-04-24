a = int(input('Enter the homework percentage: '))
b = int(input('Enter the midterm percentage: '))
c = int(input('Enter the final percentage: '))
s = a*(0.20)+b*(0.35)+c*(0.45)
print(f"Your total score is {s:.2f}")
if s >= 0 and s<=49:
    print('You receive the grade F')
elif s<55:
    print('You receive the grade D')
elif s<60:
    print('You receive the grade D+')
elif s<65:
    print('You receive the grade C')
elif s<70:
    print('You receive the grade C+')
elif s<75:
    print('You receive the grade B')
elif s<80:
    print('You receive the grade B+')
else:
    print('You receive the grade A')

