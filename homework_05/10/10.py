start_point = 0
end_point = 100
true = 1
while true:
    number = int((start_point + end_point) / 2)
    print("Is your number greater than", number, "? 1 - yes, 2 - no, 3 - it's my number")
    check = int(input())
    if check == 1:
        start_point = number
    elif check == 2:
        end_point = number
    elif check == 3:
        print("Your number is", number)
        break
