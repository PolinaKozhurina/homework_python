print("Your 8-hour working day has begun.")
hours = 1
problems = 0
result = 0
call = 0
while hours <= 8:
    print(hours, "hour.")
    hours += 1
    problems = int(input("How much problems have you already solved?\n"))
    result += problems
    call = bool(input("The wife is calling. Should I pick up the phone?\n"))
print("The working day is over. You have solved", result, "problems.")
if call == 1:
    print("You should go to the shop.")
