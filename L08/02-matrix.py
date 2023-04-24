def plus_matrix(A,B):
    ans=[[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
           ans[i][j] = A[i][j] + B[i][j]
    return ans

def mul_matrix(A,B):
    ans = [[0]*len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            x = 0
            for k in range(len(B)):
                x += A[i][k]*B[k][j]
            ans[i][j] = x
    return ans
file = input('File name: ')
matrix1,matrix2,matrix3 = [],[],[]
op = []
with open(file,'r') as fp :
    s = fp.read()
    ch = 1
    for i in s.split('\n'):
        if i!='':
            if i == '*' or i == '+' or i =='-':
                op.append(i)
                ch+=1
            else:
                lst = []
                w = i.split(' ')
                for j in w:
                    lst.append(int(j))
                if(matrix1 != [] and ch == 2):
                    matrix2.append(lst)
                elif(matrix2 != [] and ch == 3):
                    matrix3.append(lst)
                else:
                    matrix1.append(lst)
for i in op:
    if i == '*':
        x = mul_matrix(matrix1,matrix2)
    elif i == '+':
        res = plus_matrix(x,matrix3)
for i in range(len(res)):
    for j in range(len(res[0])):
        print(f"{res[i][j]:^5}",end=" ")
    print()        
#print(ch,op)
#print(matrix1,matrix2)
"""
for i in range(len(res)):
    for j in range(len(res[0])):
        print(f"{res[i][j]:^5}",end=" ")
    print()

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
*
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
+
1 0 0
0 1 0
0 0 1
if i!='' and ch == 2:
            lst = []
            if i == '*' or i == '+' or i =='-':
                op.append(i)
                ch+=1
            else:
                lst = []
                w = i.split(' ')
                for j in w:
                    lst.append(int(j))
                matrix2.append(lst)
        if i!='' and ch == 3:
            if i == '*' or i == '+' or i =='-':
                op.append(i)
                ch+=1
            else:
                lst = []
                w = i.split(' ')
                for j in w:
                    lst.append(int(j))
                matrix3.append(lst)

"""