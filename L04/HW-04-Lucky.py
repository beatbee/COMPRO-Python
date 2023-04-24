num = input()
lst = []
ch = 0
for i in num:
    lst.append(int(i))
if lst[1] == 8:
    if sum(lst)%13 == 0 and sum(lst)<56:
        print("Have bad luck.")
    else:
        print("Have good luck.")
elif lst[1] == 9:
    for i in range(len(lst)-1):
        if lst[i] == 2 and lst[i+1] == 0:
            ch = 1
            print("Have bad luck.")
            break
        elif lst[i] == 1 and lst[i+1] == 3:
            ch = 1
            print("Have bad luck.")
            break
        elif lst[i] == 1 and lst[i+1] == 8:
            ch = 1
            print("Have bad luck.")
            break
        elif lst[i] == 8 and lst[i+1] == 0:
            ch = 1
            print("Have bad luck.")
            break
        elif lst[i] == 3 and lst[i+1] == 1:
            ch = 1
            print("Have bad luck.")
            break
        elif lst[i] == 9 and lst[i+1] == 3:
            ch = 1
            print("Have bad luck.")
            break
    if ch == 0:
        print("Have good luck.")
