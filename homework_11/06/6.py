number = int(input("Введите кол-во пар синонимов: "))
dictt = {}
for i in range(number):
    first, second = input().split(" - ")
    dictt[first] = second
    dictt[second] = first
val = input("Введите слово: ")
if val in  dictt.values():
    print(dictt[input()])
else:
    print("Такого слова нет в словаре.")
