n = int(input("N: "))
m = int(input("M: "))
mod = []
for i in range(n):
    num = int(input(f"Input number {i+1}: "))
    num%=m
    if num not in mod:
        mod.append(num)
print(len(mod))
    