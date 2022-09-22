testScore = input("What did you get on the test? ")
classRank = input("What is your class rank? ")

if int(testScore) >= 80 and int(classRank) >= 50:
    print("You've been accepted congratulations!")

elif int(testScore) >= 90 and int(classRank) >= 25:
    print("You've been accepted congratulations!")

else:
    print("Sorry you've been rejected!")