n = int(input("How many animals are there in the zoo? : "))
animal = {}
for i in range(n):
    x,y = input().split()
    animal.setdefault(x,y)
q = int(input("How many questions do you want to ask? : "))
while(q>0):
    name = input()
    for i,j in animal.items():
        if name == i:
            print(j)
    if name not in animal.keys():
        print("Sorry we don't have that animal.")
    q-=1