number = int(input("Enter any integer number: \n"))
i = 1
while number // 10 != 0:
    i += 1
    number = number // 10
print("There are", i, "digits in your number")
