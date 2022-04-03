N = int(input("Enter amount of cards:\n"))
initial_cards = []
cards = input("Enter N-1 numbers of cards (from 1 to N): \n").split()
for i in range(1, N + 1):
    initial_cards.append(str(i))
result = list(set(initial_cards) ^ set(cards))
print(result)
