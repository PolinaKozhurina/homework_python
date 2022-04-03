violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
    ]
i = 0 
summ = 0 
number = int(input("Сколько песен хотите выбрать? "))
for i in range(number):
    print("Название ", i+1," песни: ")
    song = input()
    for j in range(0,9):
        if song == violator_songs[j][0]:
            summ += violator_songs[j][1]
            break
print("Время прослушивания: ", f"{summ:.2f}")
