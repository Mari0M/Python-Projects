while True:
    print("If you wish to quit type the word quit as your Name!")
    userNumber = input("Guess a number: ")
    userName = input("What is your Name: ")

    if str(userName) == "quit":
        print("Goodbye!")
        break 

    elif int(userNumber) > 10:
        print("You Win " + userName)

    elif int(userNumber) <= 10:
        print("You Lose " + userName)      
