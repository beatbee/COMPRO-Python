file = input('filename: ')
x=0
with open(file,'r') as fp:
    for i in fp.read().split('\n'):
        print(i)
        w = i.strip().split()
        for j in w:
            if 'omputer' in j:
                x+=1
print(f'Count = {x}')