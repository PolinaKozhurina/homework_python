s = input("Введите строку:")
a = set()
for i in s:
    if i in a:
        a.remove(i)
    else:
        a.add(i)
print(('можно','нельзя')[len(a)>1], 'сделать полиндром')
