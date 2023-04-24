def dec2hex(n):
  hexa = ''
  while n > 0:
    rem = n%16
    if rem < 10:
      hexa = str(n%16) + hexa
    elif rem == 10:
      hexa = 'A' + hexa
    elif rem == 11:
      hexa = 'B' + hexa
    elif rem == 12:
      hexa = 'C' + hexa
    elif rem == 13:
      hexa = 'D' + hexa
    elif rem == 14:
      hexa = 'E' + hexa
    else:
      hexa = 'F' + hexa
    n = n//16
  return hexa

## main begins here
while True:
  dec = int(input('Input Decimal: '))
  if dec == -1:
    break
  hexa = dec2hex(dec)
  print(f'Hex: {hexa}')
print('Good bye.')