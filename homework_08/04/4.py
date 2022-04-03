rows = int(input("Enter the number of rows in your theater:\n"))
seats = int(input("Enter the number of seats in the row:\n"))
distance = int(input("How many meters are between the rows?\n"))
print("The stage")
for i in range(0, rows):
    for k in range(0, seats):
        print("=", end='')
    for t in range(0, distance):
        print("*", end='')
    for k in range(0, seats):
        print("=", end='')
    print("\n")
