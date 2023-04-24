n = int(input("Number of inputs: "))
score = {}
for i in range(n):
    x,y = input().split()
    score.setdefault(x,y)
while(True):
    name = input("student: ")
    if name == '':
        print('End')
        break
    for i,j in score.items():
        if name == i:
            print(f"{i}'s score is {j}")
    
