string = input("Enter any string that contains two or more 'h' letters: \n")
string = list(string)
position_h = list(map(int, [i for i in range(len(string)) if string[i] == 'h']))
print(''.join(string[(position_h[len(position_h) - 1] - 1):position_h[0]:-1]))
