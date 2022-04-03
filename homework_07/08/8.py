N = int(input("Enter N: \n"))
summ = 0
for i in range(0, N + 1):
    summ += pow(-1, i) * pow(2, -i)
print("Sum of the row:", summ)
