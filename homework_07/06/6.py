a = int(input("Enter the left border of the segment: \n"))
b = int(input("Enter the right border of the segment: \n"))
step = int(input("Enter the step: \n"))
for x in range(b, a + 2, step):
    print("Function value:", pow(x, 3) + 2 * pow(x, 2) - 4 * x + 1)
