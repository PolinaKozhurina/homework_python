massive = input("Enter 10 integer numbers: ").split()
amount = 0
for i in range(len(massive)):
    if int(massive[i]) > 0 and int(massive[i]) % 2 == 0:
        amount += 1
print("There are", amount, "positive and even numbers in your massive.")
