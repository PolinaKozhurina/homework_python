seq = input("Location of cows:\n")
milk = 0
for i in range(len(seq)):
    if seq[i] == "b":
        milk += 2 * (i + 1)
print("Amount of milk:", milk)
