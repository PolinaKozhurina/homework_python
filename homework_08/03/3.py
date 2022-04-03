string = input("Enter any string you want: \n")
symbol = "*"
positions = []
for i in range(len(string)):
    if string[i] == symbol:
        positions.append(i + 1)
print("Positions of '*' in your string:", positions)
