import math
degree = int(input("Degree : "))
degree = ((math.pi)/180)*degree
sine = math.sin(degree)
cosine = math.cos(degree)
tann = math.tan(degree)
print(f'sin : {sine:.2f}')
print(f'cos : {cosine:.2f}')
print(f'tan : {tann:.2f}')