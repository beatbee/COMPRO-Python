def mul_matrix(A,B):
    ans = [[0]*len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            x = 0
            for k in range(len(B)):
                x += A[i][k]*B[k][j]
            ans[i][j] = x
    return ans
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]] 
print_matrix(mul_matrix(A,B))
