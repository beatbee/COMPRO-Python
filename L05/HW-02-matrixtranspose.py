def transpose_matrix(A):
    ans = [[0]*len(A) for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            ans[i][j] = A[j][i]
    return ans

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2
print_matrix(transpose_matrix(A))

