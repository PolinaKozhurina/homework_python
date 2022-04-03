dist = 0
for i in range(30, 36):
    print("How many people are in the", i, "sector?")
    people = int(input())
    if people <= 10:
        print("Everything is okay!")
    else:
        print("There are too many people!")
        dist += 1
print("The amount of disturbances is", dist)
