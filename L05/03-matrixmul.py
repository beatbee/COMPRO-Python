A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2
def mul_const(A,c):
    ans=[[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
           ans[i][j] = A[i][j]*c
    return ans
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}',end = ' ')
        print()
print_matrix(mul_const(A,c))

