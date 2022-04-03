Kostya = int(input())
Owner = int(input())
print("Кубик Кости:", Kostya)
print("Кубик владельца:", Owner)
if Kostya > Owner:
    result = (Kostya - Owner) * 1000
    print("Костя платит", result, "долларов")
elif Kostya - Owner == 0:
    result = 0
    print("Костя проиграл, но не платит")
else:
    result = (Kostya + Owner) * 1000
    print("Владелец платит", result, "долларов")
print("Игра окончена")
