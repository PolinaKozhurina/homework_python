length = int(input("Enter the length of the list:\n"))
print([1 if i % 2 == 0 else i % 5 for i in range(length)])
