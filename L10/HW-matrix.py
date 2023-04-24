class Matrix:
    def __init__(self,x):
        self.x = x
    def plus(self,B):
        self.ans=[[0]*len(self.x[0]) for i in range(len(self.x))]
        for i in range(len(self.x)):
            for j in range(len(self.x[0])):
                self.ans[i][j] = self.x[i][j] + B.x[i][j]
        return Matrix(self.ans)
    def minus(self,B):
        self.ans=[[0]*len(self.x[0]) for i in range(len(self.x))]
        for i in range(len(self.x)):
            for j in range(len(self.x[0])):
                self.ans[i][j] = self.x[i][j] - B.x[i][j]
        return Matrix(self.ans)
    def multiply(self,B):
        self.ans = [[0]*len(self.x[0]) for i in range(len(self.x))]
        for i in range(len(self.x)):
            for j in range(len(self.x[0])):
                x = 0
                for k in range(len(B.x)):
                    x += self.x[i][k]*B.x[k][j]
                self.ans[i][j] = x
        return Matrix(self.ans)
    def det(self):
        import numpy as np
        n_array = np.array(self.x)  
        det = np.linalg.det(n_array)
        return f'{det:.0f}'
    def show(self):
        self.res = self.x
        for i in range(len(self.res)):
            for j in range(len(self.res[0])):
                print(f'{self.res[i][j]:^6}',end=' ')
            print()
def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split(' ')])
    return data

print("input row of matrix A")
A = Matrix(input_matrix())
print("input row of matrix B")
B = Matrix(input_matrix())

print(f'Det of Matrix(A) = {A.det()}')
print(f'Det of Matrix(B) = {B.det()}')

print("Matrix(A+B) is:")
res = A.plus(B)
res.show()

print("Matrix(A-B) is:")
res = A.minus(B)
res.show()

print("Matrix(A*B) is:")
res = A.multiply(B)
res.show()