a = []
b = []
print("Введите первый список (3 числа): ")
for i in range(3):
    a.append(int(input()))
print("Введите второй список (7 чисел): ")
for i in range(7):
    b.append(int(input()))
a.extend(b)
a = list(set(a)) 
print(a)
