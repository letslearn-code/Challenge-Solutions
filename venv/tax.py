income = float(input("Please enter your total earnings: $"))


if(income <= 20000):

    tax_amount = income * 0.05

elif(income > 20000 and income <= 50000):

    tax_amount += (income - 20000 ) * 0.15 + 1000

elif(income > 50000 and income <= 100000):

    tax_amount += (income - 50000) * 0.25 + 5500

else:

    tax_amount += (income - 100000 ) * 0.3 + 18000


print("\nThe amount you will have after tax is: $" ,(income - tax_amount))