N = int(input('Enter the maximum number: '))
data = dict()
for i in range(N):
    data[i + 1] = 2
s = input('The required number is among these numbers: ').split()
f = 0
while s != ['Help!']:
    a = input('Answer: ')
    for elem in s:
        if a == 'Yes' and int(elem) in data:
            data[int(elem)] = 1
        if a == 'No' and int(elem) in data:
            data[int(elem)] = 0
    if len(s) == 1 and a == 'Yes':
        print('The end.')
        s = ['Help!']
        f = 1
    else:
        s = input('The required number is among these numbers: ').split()
if f == 0:
    print('Artyom could guess the following numbers: ', end='')
    for key in data:
        if data[key] == 1:
            print(key, end=' ')
            