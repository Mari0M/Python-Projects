from array import array


num_array = list()

for i in range (5):

    n = input("Input your number: 1")
    num_array.append(int(n))
    Sum = sum(num_array)

print("Your total is: " + str(Sum))