number = int(input("Enter any integer four-digit number: \n"))
print(number)
units = ((number%1000)%100)%10
tens = number//10 % 10
hundreds = number//100 % 10
thousands = number//1000
print(units * 1000 + tens * 100 + hundreds * 10 + thousands)
