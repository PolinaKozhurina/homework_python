string = input("Enter the message:\n")
counter = 1
max1 = 0
for i in range(1, len(string)):
    if string[i] == string[i-1] == "s":
        counter += 1
        if max1 < counter:
            max1 = counter
    else:
        counter = 1
print("Max 's' - substring has ", max1)
