name = input("Input name:")
lst = list(name)
for i in range(len(name)):
    lst[i] = name[i].upper()
    new1 = "".join(lst)
    print(new1)
    lst[i] = name[i].lower()


