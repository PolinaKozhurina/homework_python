rus = int(input("Enter the number of points in the Russian language: \n"))
math = int(input("Enter your math score: \n"))
inf = int(input("Enter the number of points in computer science: \n"))
if rus + math + inf >= 270:
    print("Hooray, you went to university!")
else:
    print("Congratulations! You saved your mental health!")
