X = int(input("Enter the amount of boys:\n"))
Y = int(input("Enter the amount of girls:\n"))
if X > 2 * Y or Y > 2 * X:
    print("It's impossible.")
elif X > Y:
    difference = X - Y
    for i in range(1, difference + 1):
        print("BGB", end='')
    for i in range(0, Y - difference):
        print("BG", end='')
elif Y > X:
    difference = Y - X
    for i in range(1, difference + 1):
        print("GBG", end='')
    for i in range(0, X - difference):
        print("GB", end='')
