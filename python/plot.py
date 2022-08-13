# -*- coding: utf-8 -*-

# -- Sheet --
https://datalore.jetbrains.com/view/notebook/8ds6RvvVCzF8ZqgMds5crF

print('Задание из файла "Задания_графики":')
from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(-100, 100, 10000)
y = np.arctan(-0.0012 * t ** 3 + 0.4 * t ** 2 + 0.616 * t + 6120) + 0.65 * np.sin(0.24 * t + 1.23)
- 0.27 * np.cos(0.21 * t - 0.17)
- np.sin(0.34 * t + 0.16) / (1 + 0.03 * (t - 370.5) ** 2)

plt.plot(t, y, 'r')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()

print('Строки. Задание №1:')
ss = "Today's the perfect day for learning Python, don't you think so?"
print(ss)
#1. Измените порядок символов в строке ss на обратный
ss_reversed = ""
for i in reversed(ss):
    ss_reversed += i
print(ss_reversed)

#2. Найдите подстроку заключенную между апострофами
print('Строки. Задание №2:')
substr = ""
is_substr = False
for i in ss:
    if i == "'":
        is_substr = not is_substr
        if is_substr:
            continue
    
    if is_substr:
        substr += i

print(substr)

#3. На вход подаётся строка-число. Удвойте его
print('Строки. Задание №3:')
number = "72"
doubled_number = int(number) * 2
print(number, '->', doubled_number)

#4. В строке записано два числа. Поменяйте их местами
print('Строки. Задание №4:')
two_numbers = "3254543 793423410"
first_num = ''
second_num = ''
space = None
for i in range(0, len(two_numbers)):
    if two_numbers[i] == ' ':
        space = i

for i in range(0, space):
    first_num += two_numbers[i]

for i in range(space + 1, len(two_numbers)):
    second_num += two_numbers[i]

print(two_numbers, '->', second_num, first_num)

#5. Из почтового адреса нужно достать логин
print('Строки. Задание №5:')
mail = "sasha.menkeev@mail.ru"
login = ""
bool_variable = True
for i in mail:
    if i == "@":
        bool_variable = False
    if bool_variable:
        login += i

print(mail, "->", login)

#6. Отформатировать запись номера телефона
print('Строки. Задание №6:')
phone_number = "+7 (812) 134-12-324"
correct_format = ""
for i in phone_number:
    if i != '-' and i != ' ' and i != '(' and i != ')':
        correct_format += i

print(phone_number, '->', correct_format)

#7. Определить является ли палиндромом слово или предложение
print('Строки. Задание №7:')
strings = ["Saippuakivikauppias", "А роза упала на лапу Азора", "Топот", "404", "Котёнок"]

def is_palindrome(s):
    s_without_spaces = ""
    for character in s:
        if character != ' ':
            s_without_spaces += character

    if len(s_without_spaces) % 2 == 0:
        return False
    
    s_without_spaces_reversed = ""
    for character in reversed(s_without_spaces):
        s_without_spaces_reversed += character

    if s_without_spaces.casefold() == s_without_spaces_reversed.casefold():
        return True
    else:
        return False


for string in strings:
    bool_variable = is_palindrome(string)
    if bool_variable:
        print(string, 'is a palindrome.')
    else:
        print(string, 'is not a palindrome.')

#8. Записали все числа от 1 до 123. 
#А потом зачеркнули все девятки. Какая строка получилась?
print('Строки. Задание №8:')
string = ""
string_without_9 = ""
for i in range(1, 124):
    string += str(i)
for character in string:
    if character != '9':
        string_without_9 += character

print(string_without_9)

#9. Найдите все трехзначные числа Армстронга
print('Строки. Задание №9:')
Armstrongs_numbers = []
for i in range(100, 1000):
    str_i = str(i)
    if int(str_i[0])**3 + int(str_i[1])**3 + int(str_i[2])**3 == i:
        Armstrongs_numbers.append(i)
        
print("Все трехзначные числа Армстронга:", *Armstrongs_numbers)

#10. Найдите все автоморфные числа, не превосходящие N
print('Строки. Задание №10:')
automorphic_numbers = []
N = int(input("Введите N:"))
for i in range(1, N + 1):
    str_i = str(i)
    str_ii = str(i**2)
    len_i = len(str_i)
    len_ii = len(str_ii)
    k = len_ii - len_i
    for j in range(0, len_i):
        if str_i[j] == str_ii[k]:
            k += 1
    if k == len_ii:
        automorphic_numbers.append(i)
        
print(*automorphic_numbers)

#11. Сколькими способами можно купить 185 кг штукартурки,
# если есть упаковки только по 15, 17, 21 кг?
print('Строки. Задание №11:')
count = 0
for i in range(0, int(185/15)):
    for j in range(0, int(185/17)):
        for k in range(0, int(185/21)):
            m = i*15 + j*17 + k*21
            if m > 185:
                break
            if m == 185:
                count += 1
                print(i,'*15 + ', j, '*17 + ', k, '*21', sep='')
print(count, 'способа')

