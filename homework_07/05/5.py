length = float(input("Enter the length of the letter: \n"))
width = length
amount = 0
while length > 12:
    length = length / 2
    amount += 2
    width = length
print("Amount:", amount)
