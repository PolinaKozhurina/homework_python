word = "Карамба"
lst = []
for i in range(0, 10):
    print(i + 1, ": ", end='')
    new_word = input("Что сказал пират?\n")
    lst.append(new_word)
counter = 0
lst_of_candidates = []
for i in range(1, 11):
    if lst[i-1] == word:
        counter += 1
        lst_of_candidates.append(i)
print("Количество новых пиратов:", counter)
print("Их номера в порядке следования:", lst_of_candidates)
