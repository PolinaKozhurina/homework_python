square = float(input("Enter the desired area of the flat (m^2):\n"))
price = float(input("How much does it cost? (millions)\n"))
if square >= 100:
    if price <= 10:
        print("This flat is OK.")
    else:
        print("This flat is too expensive.")
elif 100 > square >= 80:
    if price <= 7:
        print("The flat is OK.")
    else:
        print("This flat is too expensive.")
else:
    print("This flat is too small.")
