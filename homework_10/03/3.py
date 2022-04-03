import random

first = [round(random.random() * (10 - 5) + 5, 2) for i in range(20)]
second = [round(random.random() * (10 - 5) + 5, 2) for i in range(20)]
print(first)
print(second)
winners = [max(first[i], second[i]) for i in range(20)]
print(winners)
