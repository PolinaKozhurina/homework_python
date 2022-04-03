amount = int(input("How many elements are in your list?\n"))
initial_list = [int(input(f'{i + 1}: ')) for i in range(amount)]
print(initial_list)
new = [initial_list[i] for i in range(amount) if initial_list[i] != 0]
zeros = initial_list.count(0)
for j in range(zeros):
    new.append(0)
print(new)
for i in range(len(new) - 1, len(new) - zeros - 1, -1):
    new.pop(i)
print(new)
