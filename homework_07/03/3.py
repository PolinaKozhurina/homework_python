time = int(input("The timer will reset after: \n"))
flag = 0
for i in range(time, 0, -1):
    print("Do you want to neutralize the bomb?")
    answer = int(input("Yes - 1, no - 0: \n"))
    if answer == 1:
        flag = 1
        print("The bomb is neutralized", i, "seconds before the explosion.")
        break
    else:
        print(i - 1, "seconds left.")
if flag == 0:
    print("The bomb has explode.")
