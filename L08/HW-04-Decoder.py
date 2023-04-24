filepublic = input('Enter publickey filename : ')
fileprivate = input('Enter privatekey filename : ')
pb = []
pv = []
with open(filepublic,'r') as fp:
    s = fp.read()
    for i in s.split('\n'):
        pb.append(i)
with open(fileprivate,'r') as fp:
    s = fp.read()
    for i in s.split('\n'):
        pv.append(i)
#print(pb,pv)
for i in range(len(pb)):
    for j in range(len(pb[i])):
        #print(i[j])
        x = ord(pb[i][j])
        y = ord(pv[i][j])
        ans = (x+y) % 26
        #print(ans)
        if pv[i][0] >= '0' and pv[i][0]<='9': print(chr(ans+97),end='')
        else: 
            print(chr(ans+65),end='')
    print()

"""
Example 1
Enter publickey filename : publickey.txt
Enter privatekey filename : privatekey.txt
qsu
KEGI
Example 2
Enter publickey filename : publickey1.txt
Enter privatekey filename : privatekey1.txt
OSLZHVJZSKQ
PQQWOXDIBC
CUNWYQYCTVS
csuvdybmpi
ICBASKOLKLU
XUJHFNGQUZ
WARRCDLEDZW
fssclzzfih
vqchwtygcpya
mgchtzunck
"""