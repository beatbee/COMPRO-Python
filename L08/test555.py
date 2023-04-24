lst = ['a','b','c','d','e','f','A','B','C','D','E','F']
x = input()
for i in x:
    if i.isalpha() and i not in lst:
        print('ERROR')
        exit(0)
if '-' in x:
    s = '-'
    xnew = x.split('-')
    a = [x for x in xnew if len(x) == 2]
    if len(a) == len(xnew):
        print('VALID 1')
    else:
        print('ERROR')
elif '.' in x:
    s = '.'
    xnew = x.split('.')
    a = [x for x in xnew if len(x) == 4]
    if len(a) == len(xnew):
        print('VALID 3')
    else:
        print('ERROR')
elif ':' in x:
    s = ':'
    xnew = x.split('-')
    a = [x for x in xnew if len(x) == 2]
    if len(a) == len(xnew):
        print('VALID 2')
    else:
        print('ERROR')

