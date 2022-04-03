print("Enter any sequence of integer numbers:")
i = 1
counter = 0
while i != 0:
    i = int(input())
    if i % 2 == 0:
        counter += 1
print("There are", counter - 1, "even months in the sequence.")
