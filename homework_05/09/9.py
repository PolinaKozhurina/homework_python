import random

number = random.randint(0, 100)
users_number = -1
while users_number != number:
    users_number = int(input("Print your number: \n"))
    if users_number < number:
        print("Your number is less than mine. Try again.")
    elif users_number > number:
        print("Your number is more that mine. Try again.")
    else:
        print("Congratulations!")
        break
