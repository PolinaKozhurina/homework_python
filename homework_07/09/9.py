x = float(input("Enter x: \n"))
res = 1
if x % 2 == 0 and x != 0 and x < 65:
    print("Repeat input.")
    x = float(input())
for i in range(1, 7):
    res *= (x - pow(2, i) - 1)/(x - pow(2, i))
print(res)
