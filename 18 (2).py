#!/usr/bin/env python
# coding: utf-8

# Задача 1. Имена 

# In[14]:


class NumberError(Exception):
    pass

path = r"C:\Users\polin\OneDrive\Documents"
summa = 0
f = open(path + r"\people.txt", 'r')
set = f.readlines()
for line in set:
    try:
        lenght = len(line) - 1
        if lenght < 4:
            raise NumberError(f'Exception: The line { set.index(line) + 1} length is too short!')
        summa += lenght
    except NumberError as e:
        print(e)
    finally:
        f.close()
print(summa)


# Задача 2. Координаты

# In[ ]:


import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    file = open('coordinates.txt', 'r')
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        number = random.randint(0, 100)
        file_2 = open('result.txt', 'w')
        my_list = sorted([res1, res2, number])
        file_2.write(' '.join(my_list))
        
except Exception:
    print("Что-то пошло не так")
finally:
    file.close()
    file_2.close()


# Задача 3. Счастливое число

# In[17]:


import random

class Random(Exception):
    pass

path = r"C:\Users\polin\OneDrive\Documents"
summa = 0
while summa < 777:
    try:
        f = open(path + r"\file.txt", 'a')
        number = input("Enter the number:")
        ex = random.randint(1, 13)
        if ex == 1:
            raise Random("Upps! Something is wronge :(")
        summa+=int(number)
        f.write(number + '\n')
    except Random as e:
        print(e)
    finally:
        f.close()


# Задача 4. Регистрация

# In[32]:


class ValueErrorm(Exception):
    pass

class NameErrorm(Exception):
    pass

class SyntaxErrorm(Exception):
    pass

path = r"C:\Users\polin\OneDrive\Documents"
f = open(path + r"\registrations.txt", 'r', encoding='utf-8')
set = f.readlines()
for line in set:
    try:
        lines = line.split()
        if len(lines) < 3 or (int(lines[2]) < 10) or (int(lines[2]) > 99):
            raise ValueErrorm
        if lines[0].isalpha() == 0:
            raise NameErrorm
        if ('@' not in str(lines[1])) or ('.' not in str(lines[1])):
            raise SyntaxErrorm
    except NameErrorm:
        print(f"Check Name in line {set.index(line) + 1} ")
    except SyntaxErrorm:
        print(f"Check email in line {set.index(line) + 1} ")
    except ValueErrorm:
        print(f"Check data in line {set.index(line) + 1} ")                                      
    finally:
        f.close()


# Задача 5. Текстовый калькулятор

# In[54]:


class SyntaxErr(Exception):
    pass

class ValueErr(Exception):
    pass

class NullErr(Exception):
    pass

list_oper = ['+', '-', '*', '/', 'div', 'mod']
    
            

summa = 0 
path = r"C:\Users\polin\OneDrive\Documents"
f = open(path + r"\calc.txt", 'r', encoding='utf-8')
set = f.readlines()
try:
    for line in set:
        lines = line.split()
        if len(lines)!=3 or (lines[1] not in list_oper):
            raise SyntaxErr
        if not (lines[0].isnumeric() or lines[2].isnumeric()):
            raise ValueErr
        x = int(lines[0])
        y = int(lines[2])
        if lines[1] == '+':
            summa += (x+y)
        elif lines[1] == '-':
            summa += (x-y)
        elif lines[1] == '*':
            summa += (x*y)
        elif lines[1] == '/':
            if y==0:
                raise NullErr
            summa += (x/y)
except SyntaxErr:
    print(f"Syntax error in line {set.index(line) + 1}\n")
except ValueErr:
    print(f"Value error in line {set.index(line) + 1}\n")
except NullErr:
    print(f"Null error in line {set.index(line) + 1}\n")
finally:
    f.close()
print(summa)


# Задача 6. Чат

# In[ ]:


user = input('Введите имя: ')

while True:
    print('Чтобы посмотреть текущий текст чата - введите <0>')
    print('Чтобы отправить сообщение - введите <1>')
    action = input()

    if action == '0':

        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                for i_message in file:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История сообщений пуста. \n')

    elif action == '1':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write(f' { user } : { message } \n')
    else:
        print('Такой команды нет')


# Задача 7. Текстовый калькулятор 2

# In[63]:


class SyntaxErr(Exception):
    pass

class ValueErr(Exception):
    pass

class NullErr(Exception):
    pass

list_oper = ['+', '-', '*', '/', 'div', 'mod']
    


summa = 0 
path = r"C:\Users\polin\OneDrive\Documents"
f = open(path + r"\calc.txt", 'r', encoding='utf-8')
set = f.readlines()
try:
    for line in set:
        lines = line.split()
        if len(lines)!=3 or (lines[1] not in list_oper):
            raise SyntaxErr
        if not (lines[0].isnumeric() or lines[2].isnumeric()):
            raise ValueErr
        x = int(lines[0])
        y = int(lines[2])
        if lines[1] == '+':
            summa += (x+y)
        elif lines[1] == '-':
            summa += (x-y)
        elif lines[1] == '*':
            summa += (x*y)
        elif lines[1] == '/':
            if y==0:
                raise NullErr
            summa += (x/y)
except SyntaxErr:
    print(f"Syntax error in line {set.index(line) + 1}\n")
    answ = input("Do you want correct? ")
    if answ == 'yes':
        line = input("Enter:\n")
        f.writelines(lines)
except ValueErr:
    print(f"Value error in line {set.index(line) + 1}\n")
    answ = input("Do you want correct? ")
    if answ == 'yes':
        line = input("Enter:\n")
        f.writelines(lines)
except NullErr:
    print(f"Null error in line {set.index(line) + 1}\n")
    answ = input("Do you want correct? ")
    if answ == 'yes':
        line = input("Enter:\n")
        f.close()
        f = open(path + r"\calc.txt", 'w', encoding='utf-8')
        f.writelines(set)
finally:
    f.close()
print(summa)


# In[ ]:




