def What(x):
    x = str(x)
    if x.islower():
        return 'Album'
    else:
        return 'Photobook'

def SStatus():
    return x
def RReal(x):
    if(ord(x[0])+1) == ord(x[-1]):
        return True
    else:
        return False

word = input()
x = What(word)
z = RReal(word)
print(x)
print(z)