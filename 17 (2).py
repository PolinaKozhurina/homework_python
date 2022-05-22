#!/usr/bin/env python
# coding: utf-8

# Задача 1. Сумма чисел 2

# In[16]:


def adder(new):
    summ = 0
    for n in new:
        summ += n
    return summ


path = r"C:\Users\polin\OneDrive\Documents"
f = open(path + r"\text.txt", 'r')
my_lines = f.readlines()
lst2 = []
for line in my_lines:
        strs = line.split(' ')
        for s in strs:
            if s != '' and s!= '\n':
                lst2 = lst2 + [int(s)]
my_file = open(path + r"\answer.txt", "w")
my_file.write(str(adder(lst2)))
print(adder(lst2))
my_file.close()
f.close()


# Задача 2. Дзен Пайтона

# In[19]:


path = r"C:\Users\polin\OneDrive\Documents"
file = open(path + r"\zen.txt", 'r')
s = file.readlines()
s.reverse()
print(''.join(s).strip('\n'))


# Задача 3. Дзен Пайтона 2

# In[20]:


lines = 0
words = 0
letters = 0
path = r"C:\Users\polin\OneDrive\Documents"
file = open(path + r"\zen.txt", 'r')


for line in file:
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)


# Задача 4. Файлы и папки

# In[85]:


import os

path = r"C:\Users\polin\OneDrive\Documents"

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


print(get_size(path))


# Задача 5. Сохранение

# In[103]:


import os

def save_files(string):
    way = str(input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): '))
    way = way + " "
    filename = str(input('Введите имя файла: '))
    r_path = way.replace(" ", r"\")
    real_path = (r_path + filename)
    path = str(r'C:\' + real_path)
    check_file = os.path.exists(path)
    print(check_file)
    if check_file:
        print('Файл с таким именем уже существует!')
        ans = input('Вы действительно хотите перезаписать файл? ').lower()
        if ans == 'yes':
            f = open(path, 'w')
            f.write(string)
            print('Файл успешно перезаписан!')
        else:
            print('Файл не перезаписан')
    else:
        f = open(path, 'w')
        f.write(string)
        print('Файл успешно сохранён!')

text = input('Введите строку: ')
save_files(text)


# Задача 6. Паранойя

# In[44]:


path = r"C:\Users\polin\OneDrive\Documents"
f = open(path + r"\text1.txt", 'r')
s = f.readlines()


def ces(step, text):
    alphabet=[]
    for i in range(97,123):
        alphabet.append(chr(i))
    lenn = len(alphabet)
    encrypted_text = []
    for i in range(len(text)):
        symbol = text[i]
        if symbol in alphabet:
            letter = alphabet.index(symbol)
            if letter + step < lenn:
                symbol = alphabet[letter + step]
            else:
                symbol = alphabet[letter + step - lenn]
            encrypted_text.append(symbol)
        else:
            encrypted_text.append(text[i])
    return encrypted_text


i = 0
my_file = open(path + r"\cipher_text.txt", "w")
for line in s:
    i+=1
    my_file.write(str.capitalize(''.join(ces(i, line.lower()))))
my_file.close()


# Задача 7. Турнир

# In[ ]:


path = r"C:\Users\polin\OneDrive\Documents"
f = open(path + r"\first_tour.txt", 'r')
k = int(new_file.readline())
 
new_list = []
 
for line in new_file:
    new_line = line.split()
 
    if int(new_line[-1]) > k:
        new_list.append(new_line)
    
 
new_list.sort(key=lambda a: int(a[-1]))
new_list.reverse()
 
count = str(len(new_list))
# счетчик победителей вышедших во второй тур count
out_lst = []
for i in new_list:
    name_sim = str(i[-2][1])+'.'
    s_win = list(name_sim + str(i[1]) + str(i[-1]))
    out_lst.append(s_win)

with open("second_tour.txt", "a+", encoding='utf-8') as f_out:
    f_out.write(count)
    f_out.write(out_lst)
 
for i, val in enumerate(out_lst, start=1):
    print(f' {i} ) {str(val)}')
new_file.close()


# Задача 8. Частотный анализ

# In[65]:


import string

dict1 = {}
path = r"C:\Users\polin\OneDrive\Documents"
f = open(path + r"\text1.txt", 'r')
t = f.readlines()
spec_chars = string.punctuation + '\n\xa0«»\t—…'
spec_chars = list(spec_chars)
for line in t:
    line = line.lower()
    
    for sp in spec_chars:
        if sp in line:
            line = line.replace(sp, '')
    for simbol in line:
        if simbol in dict1.keys():
            dict1[simbol] += 1
        else:
            dict1[simbol] = 1
    
summa = sum(dict1.values())
for key in dict1.keys():
    dict1[key] /= summa
    
sorted_values = sorted(dict1.values())
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break
print(dict1)


# Задача 9. Война и мир

# In[107]:


import zipfile, string


archive = r"\voyna-i-mir.zip"
path = r"C:\Users\polin\OneDrive\Documents"
with zipfile.ZipFile(path + archive, 'r') as zip_file:
    zip_file.extractall(path + r"\voyna-i-mir")
    f = open(path + r"\voyna-i-mir\voyna-i-mir.txt", encoding='utf-8')
    
dict1 = {}
t = f.readlines()
print(t)
spec_chars = string.punctuation + '\n\xa0«»\t—…1234567890°№“„–'
spec_chars = list(spec_chars)
for line in t:
    line = line.lower()
    
    for sp in spec_chars:
        if sp in line:
            line = line.replace(sp, '')
    for simbol in line:
        if simbol in dict1.keys():
            dict1[simbol] += 1
        else:
            dict1[simbol] = 1

sorted_values = sorted(dict1.values())
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break
print(dict1)


# In[108]:


import zipfile


archive = r'zip.zip'
file_path = os.path.join('zip', 'test.txt')
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall(r'zip')
    f = open(file_path, encoding='utf-8')
    f.close()

with open(file_path) as inf:
    print(inf.read())


# In[109]:


path = r"C:\\Users\\polin\\OneDrive\\Documents\\text.txt"
f = open(path)


# In[ ]:




