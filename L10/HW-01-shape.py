class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)
    def is_square(self):
        if self.w == self.l:
            return 'This rectangle is square too.'
        else:
            return 'This rectangle is not square.'
class Triangle:
    def __init__(self,a,b,c):
        self.a = l1
        self.b = l2
        self.c =l3
    def area(self):
        s = (self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(0.5)
    def perimeter(self):
        return self.a+self.b+self.c
    def is_right_triangle(self):
        ch = 0
        if self.a<=self.b<=self.c or self.b<=self.a<=self.c:
            if self.c**2 == self.a**2 + self.b**2:
                ch = 1
        elif self.a<=self.c<=self.b or self.c<=self.a<=self.b:
            if self.b**2 == self.a**2 + self.c**2:
                ch = 1
        elif self.b<=self.c<=self.a or self.c<=self.b<=self.a:
            if self.a**2 == self.b**2 + self.c**2:
                ch = 1
        if ch:
            return 'This triangle is right triangle too.'
        else:
            return 'This triangle is not right triangle.'
        
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        ans = 3.14*(r**2)
        return round(ans,2)
    def perimeter(self):
        ans1 = 2*3.14*r
        return round(ans1,2)
l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area()}.')  
print(f'Perimeter is {p3.perimeter()}.')
"""
class Rectangle:
    def __init__(self,l,w):
        self.l = int(l)
        self.w = int(w)
    def area(self):
        return f'{self.l*self.w:.0f}'
    def perimeter(self):
        return f'{2*(self.l+self.w):.0f}'
    def is_square(self):
        if self.l == self.w:
            return 'This rectangle is square too.'
        else:
            return 'This rectangle is not square.'
        
class Triangle:
    def __init__(self,l1,l2,l3):
        self.l1 = int(l1)
        self.l2 = int(l2)
        self.l3 = int(l3)
    def area(self):
        s = (self.l1+self.l2+self.l3)/2
        return f'{(s*(s-self.l1)*(s-self.l2)*(s-self.l3))**0.5}'
    def perimeter(self):
        return f'{self.l1+self.l2+self.l3:.0f}'
    def is_right_triangle(self):
        x, y, z = sorted([self.l1,self.l2,self.l3])
        if x**2 == z**2+y**2:
            return 'This triangle is right triangle too.'
        else:
            return 'This triangle is not right triangle.'
class Circle:
    def __init__(self,r):
        self.r = int(r)
    def area(self):
        return f'{((self.r)**2)*3.14:.2f}'
    def perimeter(self):
        return f'{(self.r)*2*3.14:.2f}'
l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area()}.')  
print(f'Perimeter is {p3.perimeter()}.') 
"""