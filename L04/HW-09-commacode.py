def commaCode(myList):
    ch = 0
    for i in myList:
        if ch == len(myList)-2:
            print(i,end=', and ')
            ch+=1
        elif ch == len(myList)-1:
            print(i)
        else:
            print(i,end=', ')
            ch+=1
lst = [x for x in input("Input: ").split()]
commaCode(lst)
