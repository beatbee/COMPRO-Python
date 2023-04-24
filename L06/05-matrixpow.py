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
            print(f'{A[i][j]:^6}', end = ' ')
        print()
A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2
print_matrix(power_matrix(A,2))