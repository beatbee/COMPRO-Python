import sys
d = int(input("Enter the depth of the well: "))
j = int(input("Enter the height the frog can jump up: "))
s = int(input("Enter the height the frog slips down: "))
ans = d
day = 0
if d>j and s>=j:
    print("The frog is always stuck in the well.")
    sys.exit()
while(ans>0):
    day+=1
    ans-=j
    if ans <= 0 :
        break
    print(f'On day {day} the frog leaps to the depth of {ans} meters.')
    ans+=s
    print(f'At night he slips down to the depth of {ans} meters.')
print(f'The frog can escape the well on day {day}.')
    
    
