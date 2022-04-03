from collections import Counter

string = input("Введите строку: ")
lst = list(string)
no_inv_map = dict(Counter(lst))
print(no_inv_map)
inv_map = {}
for k, v in no_inv_map.items():
    inv_map[v] = inv_map.get(v, [])
    inv_map[v].append(k)
print(inv_map)
