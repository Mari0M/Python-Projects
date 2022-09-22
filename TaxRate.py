salesTax = input("Input the sales tax rate in decimal form: ")

salesPrice = input("Input the sales price: ")

amountOfTax = (float(salesTax)/100) * float(salesPrice)
finalPrice = float(salesPrice) - float(amountOfTax)
print(("Your taxed amount is: $") + str(amountOfTax))
print(("Your total price is: $") + str(finalPrice))
quit