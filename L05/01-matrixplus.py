A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
def plus_matrix(A,B):
    ans=[[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
           ans[i][j] = A[i][j] + B[i][j]
    return ans
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}',end = ' ')
        print()
print_matrix(plus_matrix(A,B))


