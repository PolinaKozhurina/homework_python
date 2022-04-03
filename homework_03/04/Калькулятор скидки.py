first = int(input("Enter the cost of 1 chair: \n"))
second = int(input("Enter the cost of 2 chair: \n"))
third = int(input("Enter the cost of 3 chair: \n"))
summ = first + second + third
if summ > 10000:
    print("Amount payable (including 10% discount): \n", f'{summ - 0.10 * summ:.1f}')
else:
    print("Amount payable:", summ)
