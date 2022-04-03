number = int(input("Enter any integer number:\n"))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(number, "!=", factorial)
