class py_solution:
    def __init__(self,p):
        self.p = p
    def is_valid_parentheses(self):
        l = ['(','[','{']
        r = [')',']','}']
        ch = 0
        for i in self.p:
            if i in l:
                for j in self.p:
                    if j in r:
                        ch +=1
            if i in r:
                for j in self.p:
                    if j in l:
                        ch +=1
        if ch > 2*len(self.p):
            return True
        else:
            return False


n = input('input: ')
b = py_solution(n)
if b.is_valid_parentheses(): 
    print('valid parentheses')
else: 
    print('invalid parentheses')