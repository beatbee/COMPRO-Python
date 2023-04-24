D = {}
while(True):
    id = int(input("Student ID : "))
    if id == 0:
        break
    y = int(input("years : "))
    D[id] = y
sy = int(input("Separate year: "))
for i,j in D.items():
    if j>=sy:
        print(i) 
"""
Student ID : 1
years : 4
Student ID : 2
years : 1 
Student ID : 3
years : 2
Student ID : 4
years : 1
Student ID : 0
Separate year: 2
1
3
"""
