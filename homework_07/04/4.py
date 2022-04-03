a = int(input("Enter the left border of the segment: \n"))
b = int(input("Enter the right border of the segment: \n"))
c = int(input("Enter the delimiter: \n"))
summ = 0
amount = 0
for i in range(a, b + 1):
    if i % c == 0 and i != 0:
        summ += i
        amount += 1
print("Average: ", summ / amount)
