velocity = float(input("Enter velocity: \n"))
hours = float(input("Enter amount of hours: \n"))
path = velocity * hours
rounds = path // 115
print(path - rounds * 115)
