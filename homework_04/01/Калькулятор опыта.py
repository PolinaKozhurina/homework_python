points = int(input("Enter the number of points: \n"))
if points < 1000 :
    print("Your level is 1")
elif points < 2500 :
    print("Your level is 2")
elif points < 5000:
    print("Your level is 3")
else:
    print("Your level is 4")
