scholarship = float(input("Enter the scholarship: \n"))
utility_bills = float(input("Enter utility bills: \n"))
summ = utility_bills
for i in range(2, 11):
    utility_bills *= 1.03
    summ += utility_bills
print("You need to ask parents for", round(summ - scholarship * 10, 3), "dollars")
