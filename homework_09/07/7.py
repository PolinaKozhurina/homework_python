favorite_films = []
films = ['The Green Mile', 'The Lord of the Rings', 'Schindlers List', 'Back to the Future', 'Intouchables']
number = int(input("How many movies do you want to add? "))
for i in range(number):
    k = 0 
    film = input("Enter movie title: ")
    for j in range(len(films)):
        if film == films[j]:
            favorite_films.append(film)
            k+=1
    if k == 0 :
        print("Error, we don't have the film " + film)
print("List of your favorite films:")
for x in favorite_films: print(x)
