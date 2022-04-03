mileage = int(input("Введите пробег: \n"))
day = int(input("Введите сегодняшнее число: \n"))
summ = 0
residue = 1
mileage_new = mileage
while residue != 0:
    residue = mileage % 10
    summ = summ + residue
    mileage = mileage // 10
if summ > day:
    print("Сброс.")
    print("Пробег: 0.")
else:
    print("Сегодня не поломался.")
    print("Пробег: ", mileage_new)
