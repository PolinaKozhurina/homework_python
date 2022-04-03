for number in range(10, 100):
    units = number % 10
    tens = number // 10
    if number == 3 * units * tens:
        print(number)
