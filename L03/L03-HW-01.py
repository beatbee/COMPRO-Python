import math
def inputShape():
    n = int(input("Input Shape: "))
    return n

def calculateSphere():
    r = int(input("Input radius(meter): "))
    v = (4/3)*math.pi*(r**3)
    print(f'The volume is {v:.2f} cubic meter.')
    return v

def calculateCone():
    r = int(input("Input radius(meter): "))
    h = int(input("Input height(meter): "))
    v = (1/3)*math.pi*(r**2)*h
    print(f'The volume is {v:.2f} cubic meter.')
    return v

def calculateCylinder():
    r = int(input("Input radius(meter): "))
    h = int(input("Input height(meter): "))
    v = math.pi*(r**2)*h
    print(f'The volume is {v:.2f} cubic meter.')
    return v

def calculatePrism():
    w = int(input("Input width(meter): "))
    l = int(input("Input length(meter): "))
    h = int(input("Input height(meter): "))
    v = l*h*w
    print(f'The volume is {v:.2f} cubic meter.')
    return v
    
def calculatePyramid():
    w = int(input("Input width(meter): "))
    l = int(input("Input length(meter): "))
    h = int(input("Input height(meter): "))
    v = l*h*w/3
    print(f'The volume is {v:.2f} cubic meter.')
    return v

def calculatePrice(v):
    p = int(input("Price(Bath) per 1 cubic meter: "))
    print(f"The price is {v*p:.2f} Baht.")

n = inputShape()
if(n == 1): v = calculateSphere()
elif(n == 2): v = calculateCone()
elif(n == 3): v = calculateCylinder()
elif(n == 4): v = calculatePrism()
else: v = calculatePyramid()
calculatePrice(v)
