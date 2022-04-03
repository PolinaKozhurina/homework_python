numbers = [114, 12, 14, 10605, 4907, 450]
for number in numbers:
    if number % 2 == 0 and number % 3 != 0:
        print("Number", number, "is appropriate.")
    else:
        print("Number", number, "isn't appropriate.")
