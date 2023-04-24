A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2
def plus_matrix(A,B):
    ans=[[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
           ans[i][j] = A[i][j] + B[i][j]
    return ans
def minus_matrix(A,B):
    ans=[[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
           ans[i][j] = A[i][j] - B[i][j]
    return ans
def transpose_matrix(A):
    ans = [[0]*len(A) for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            ans[i][j] = A[j][i]
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
def power_matrix(A,c):
    for a in range(c-1):
        if a == 0:B=A
        else: B=ans
        ans = [[0]*len(A[0]) for i in range(len(B))]
        for i in range(len(B)):
            for j in range(len(A[0])):
                x = 0
                for k in range(len(A)):
                    x += B[i][k]*A[k][j]
                ans[i][j] = x
    return ans
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}',end = ' ')
        print()
print_matrix(mul_matrix(plus_matrix(A,transpose_matrix(B)),minus_matrix(power_matrix(C,2),D)))