#Geting input from user for total earnings.
income = float(input("Please enter your total earnings: $"))
#Variable for amount being taxed.
tax_amount = 0
#Variable for the amount the person will receive after being taxed.
take_home = 0

if(income <= 20000):
    #Calculating 5%
    tax_amount = income * 0.05

    #Calulating take home by removing tax_amount from income.
    take_home = income - tax_amount

    print("The amount you will have after tax is: $" + str(take_home))

elif(income > 20000 and income <= 50000):
    #Tax from previous bracket which equals $1,000
    tax_amount = 1000

    #Calculating tax amount of 15%(Taking away 20k due to it already being taxed)
    tax_amount += (income - 20000 )* 0.15

    # Calulating take home by removing tax_amount from income.
    take_home = income - tax_amount
    print("The amount you will have after tax is: $" + str(take_home))

elif(income > 50000 and income <= 100000):
    #Tax from previous tax brakets which equals $5,500
    tax_amount = 5500

    #Calculating tax amount of 25%(Taking away 50k due to already being taxed)
    tax_amount += (income - 50000) * 0.25

    # Calulating take home by removing tax_amount from income.
    take_home = income - tax_amount

    print("The amount you will have after tax is: $" + str(take_home))

else:
    #Tax from previous tax brakets which equals $18,000
    tax_amount = 18000

    # Calculating tax amount of 30%(Taking away 100k due to already being taxed)
    tax_amount += (income - 100000 )* 0.3

    take_home = income - tax_amount
    print("The amount you will have after tax is: $" + str(take_home))