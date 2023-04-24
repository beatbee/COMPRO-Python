code = '''
def showO(n):
    for q in range(n):
        for i in range(n//2+1):
            print((' '*((n-1)//2-i) + 'O'*(2*(i)+1) + ' '*((n-1)//2-i))*n)
        for j in range(1,(n-1)//2 +1):
            print((' '*(j) + 'O'*(n-(2*j)) + ' '*(j))*n)'''
with open('printO.py', 'w') as f:
  f.write(code)
import printO
printO.showO(int(input()))
