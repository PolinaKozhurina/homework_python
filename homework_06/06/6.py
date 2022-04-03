import random

number = int(input("How many pupils are in the class?\n"))
grade = 0
A = 0
B_C = 0
D = 0
for i in range(1, number + 1):
    grade = random.randint(3, 5)
    if grade == 3:
        D += 1
    elif grade == 4:
        B_C += 1
    else:
        A += 1
print("5:", A, ";", "4:", B_C, ";", "3:", D)
if A > B_C and A > D:
    print("More excellent students today:")
elif B_C > A and B_C > D:
    print("More good pupils today.")
else:
    print("More average pupils today.")
