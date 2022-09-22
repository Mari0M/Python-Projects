amount1 = input("What is amount 1? ")
amount2= input("What is amount 2? ")

if int(amount1) > 10 and int(amount2) < 100:
    
    if int(amount1) > int(amount2):
        
        print("The greater amount is amount 1 at a value of: " + amount1)
    
    else:

        print("The greater amount is amount 2 at a value of: " + amount2)

else:

    print("That was an invalid option. Goodbye!")