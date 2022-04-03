name = input("Enter your name: \n")
debt = float(input("Enter your debt: \n"))
print(name, ",your debt is", debt, ".")
i = 0
while i < debt:
    print("How much will you deposit right now to pay it off?")
    i = float(input())
    if i < debt:
        print("It's not enough to pay your debt off. Do it again.")
print("Well, you have successfully pay the debt off. Thank you!")
