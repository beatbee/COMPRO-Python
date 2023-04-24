a = int(input("Number of TVs: "))
b = int(input("Number of DVD players: "))
c = int(input("Number of audio systems: "))
price = a*600 + b*150 + c*300
print(f"The total amount is {price:.2f} baht.")
if price >= 2000:
    print(f"Discount: {price*5/100:.2f} baht.")
    print(f"Your payment is {price*95/100:.2f} baht. Thank you.")
else:
     print(f"Your payment is {price:.2f} baht. Thank you.")