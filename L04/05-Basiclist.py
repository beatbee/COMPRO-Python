Inte = []
ch = 0
while(True):
    n = int(input("Enter a positive number: "))
    if n > 0:
        ch+=1
        Inte.append(n)
    if ch == 5:
        break
Inte.sort()
med = Inte[len(Inte)//2]
print(f"sum: {sum(Inte)}")
print(f"min: {min(Inte)}")
print(f"max: {max(Inte)}")
print(f"med: {med}")
