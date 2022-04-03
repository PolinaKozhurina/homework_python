place = int(input("Enter your place on the list:\n"))
if place < 11:
    print("Hooray, you went to university!")
    points = int(input("Enter the number of points you have:\n"))
    if points >= 290:
        print("Congratulations! You will receive a scholarship!")
    else:
        print("Unfortunately, your points are too low for a scholarship.")
else:
    print("Congratulations! You saved your mental health!")
