def create_zero_matrix(m,n):
     return [[0]*n for i in range(m)]
print(create_zero_matrix(2,3))
print(create_zero_matrix(7,5))
print(create_zero_matrix(10,10))
def plus(A,B):
     return [[A[y][i]+B[y][i] for i in range(len(A[0]))] for y in range(len(A))]
print(plus([[1,2],[3,4]],[[5,6],[7,8]]))
print(plus([[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]))
print(plus([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]],[[12,23,34,45,56],[32,43,46,57,78],[51,63,59,80,71]]))
def transpose(A):
     return [[x[i] for x in A] for i in range(len(A[0]))]
print(transpose([[1,2],[3,4]]))
print(transpose([[1,2],[3,4],[5,6]]))
print(transpose([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]]))
def multiply(A,B):
     return  [[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))]

print(multiply([[1,2],[3,4]],[[5,6],[7,8]]))
print(multiply([[1,2],[3,4],[5,6]],[[7,8],[9,10]]))
print(multiply([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]],[[12,23,34,45,56,44],[32,43,46,57,78,33],[51,63,59,80,71,22],[1,2,3,4,5,34],[6,7,8,9,10,99]]))