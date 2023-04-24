a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if (a<=15 and b<=10 and c<= 8) :
    print("Box size 1")
elif a<=25 and b<=15 and c<= 12:
    print("Box size 2")
elif a<=50 and b<=40 and c<= 20:
    print("Box size 3")
else:
    print("Oversize product")


