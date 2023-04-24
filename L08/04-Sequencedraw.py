file = input('File name: ')
draw = {}
with open(file,'r') as fp:
    s = fp.read()
    for i in s.split('\n'):
        #lst = []
        if i == '0':
            break
        if i >= '1' and i<='9':
            ch = int(i)
        elif ch in draw :
            draw[ch].append(i)
        else:
            draw[ch] = [i]
for i in sorted(draw):
    for j in range(len(draw[i])):
        print(draw[i][j])
        
