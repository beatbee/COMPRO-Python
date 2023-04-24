file = input('File name: ')
sen = 0
with open(file,'r') as fp:
    s = fp.read()
    for i in s.split('.'):
        sen+=1
print(f'There are {sen-1} sentences and {len(s.split())} words.')
