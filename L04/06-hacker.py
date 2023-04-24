pwd = list(input())
ch = 0
for i in pwd:
    guess = input()
    if guess == i:
        ch+=1
    else:
        print("Fail!!")
        break
if ch == len(pwd) :
    print('Succeed!!')
    