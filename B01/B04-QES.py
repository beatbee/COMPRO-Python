import sys
import math
a = float(input("Enter 1st coefficient: "))
if a == 0:
    print("1st coefficient can't be zero. Program exits.")
    sys.exit()
b = float(input("Enter 2st coefficient: "))
c = float(input("Enter 3st coefficient: "))
d = (b**2)-(4*a*c)
if d > 0:
   ans1 = ( -b + d**(1/2) ) / (2*a)
   ans2 = ( -b - d**(1/2) ) / (2*a)
   print(f"There are two real roots: {ans1:.3f} and {ans2:.3f}")
elif d == 0:
    ans = (-b)/(2*a)
    print(f"One real root: {ans:.3f}")
else:
    ans = -b/(2*a)
    ans1 = (math.sqrt(-d))/(2*a)
    if a< 0:
        ans1 = -ans1
        print(f"There are two complex roots: {ans:.3f}+{ans1:.3f}i and {ans:.3f}-{ans1:.3f}i")
    if a>0:
         print(f"There are two complex roots: {ans:.3f}+{ans1:.3f}i and {ans:.3f}-{ans1:.3f}i")
    

