deposit = float(input("Enter your deposit here:\n"))
percent = int(input("What is the annual percent, %?\n"))
result = float(input("What is the final sum?\n"))
years = 0
while deposit < result:
    years += 1
    deposit = deposit * (1 + percent / 100)
    deposit = round(deposit)
print("You need", years, "years to reach desired sum.")
