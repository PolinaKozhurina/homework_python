debtors = int(input("How many debtors are there? \n"))
summ = 0
debt = 0
for i in range(0, debtors, 5):
    print("The debtor number", i)
    debt = int(input("Enter you debt: "))
    summ += debt
print("The summa of the debt:", summ)
