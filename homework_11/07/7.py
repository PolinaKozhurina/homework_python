number = int(input('Введите кол-во заказов: '))
dictt = {}
for _ in range(number):
    order = input()
    name, pizza, amount = order.rsplit(maxsplit=3) #Разбивает строку на части, используя разделитель, и возвращает эти части списком. Направление разбиения: справа налево.
    amount = int(amount)
    if name not in dictt:
        dictt[name] = {pizza: amount}
    else:
        if pizza not in dictt[name]:
            dictt[name] |= {pizza: amount}
        else:
            dictt[name][pizza] += amount
for name, order in sorted(dictt.items()):
    print(f'{name}:')
    for pizza, amount in sorted(order.items()):
        print('    ', pizza, amount)
    