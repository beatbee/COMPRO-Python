name = input("Input name: ")
lst = list(name)
verse = list(name[::-1])
verse1 = list(name[::-1])
for i in range(len(name)):
    lst[i] = name[i].upper()
    verse1[i] = verse[i].upper()
    for j in range(len(name)):
        if name[j] == name[i]:
            lst[j] = name[j].upper()
        if verse[j] == verse[i]:
            verse1[j] = verse[j].upper()   
    new1 = "".join(lst)
    new2 = "".join(verse1)
    print(new1,new2)
    lst = list(name)
    verse1 = list(verse)
    
    
 

