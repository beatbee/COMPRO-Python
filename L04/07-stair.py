def draw(m):
    for i in range(len(m)):
        print(m[i]*(i+1),end='\n')
while(True):
    stair = [x for x in input().split()]
    if(stair[0] == '0'):
        break
    draw(stair)
print("Good Bye.")