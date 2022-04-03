amount_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке?: '))
print('Значит, выбывает каждый', number, 'человек')
list_people = list(range(1, amount_people + 1))
count = 0
while len(list_people) > 1:
    print('Текущий круг людей: ', list_people)
    print('Начало счёта с номера:', list_people[count])
    count = (count + number - 1) % len(list_people)
    if list_people[count] == list_people[-1]:
        print('Выбывает человек под номером:', list_people.pop(count))
        count = 0
    else:
        print('Выбывает человек под номером:', list_people.pop(count))
print('Остался человек под номером:', list_people[0])
