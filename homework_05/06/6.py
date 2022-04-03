i = 1
counter_pos = 0
counter_neg = 0
while i != 0:
    print("Enter your grade: ")
    i = int(input())
    if i > 0:
        counter_pos += 1
    elif i < 0:
        counter_neg += 1
print("There are", counter_pos, "positive grades.")
print("There are", counter_neg, "negative grades.")
