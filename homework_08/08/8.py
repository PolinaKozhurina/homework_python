sign = int(input("Enter the length of the title:\n"))
exc = int(input("Enter the number of exclamation marks:\n"))
row = 1
for i in range(row):
  rows = '~' * sign
  rows = rows + '!' * exc + rows
  print()
  print(rows)
