n = int(input("Enter initial amount in Baht: "))
m = int(input("Enter interest rate in percent: "))
#1
ans1 = n*((100+m)/100)
print(f'Total amount after 1 year is {ans1:.2f} Baht.')
#5
ans5 = n*(((100+m)**5)/(100**5))
print(f'Total amount after 5 years is {ans5:.2f} Baht.')
#10
ans10 = n*(((100+m)**10)/(100**10))
print(f'Total amount after 10 years is {ans10:.2f} Baht.')
#20
ans20 = n*(((100+m)**20)/(100**20))
print(f'Total amount after 20 years is {ans20:.2f} Baht.')