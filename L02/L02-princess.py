n = int(input('s: '))
h = n//3600
m = (n-(3600*h))//60
s = n%60
print(f'{n} seconds equals {h} hour(s) {m} minute(s) and {s} second(s)')