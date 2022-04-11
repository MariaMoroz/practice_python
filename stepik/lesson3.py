# def f(x):
#     if x <= -2:
#         return 1 - (x + 2)**2
#     elif -2 < x <= 2:
#         return -x/2
#     elif x > 2:
#         return (x - 2)**2 +1
# print(f(1))

# ***
# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка
# def modify_list(l):
#     for i in range(len(l)-1,-1,-1):
#         if l[i] % 2 == 1:
#             l.remove(l[i])
#         else:
#             l[i]=l[i]//2
#
# lst = [10, 5, 5, 8, 3]
#
# modify_list(lst)
# print(lst)

# d = {'a': 239, 10: 100}
# d['a'] = [239]
# for key in d:
#     d[key] = [d.get(key)]
# print(d.keys()) #dict_keys(['a', 10])
# print(d.values()) #dict_values([239, 100])
# print(d.keys())

# print(d) #{'a': [239, 3], 10: 100}
# ***
# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.
#
# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# Если к [pлюча key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
# Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь и сопоставить ему список из переданного элемента [value].
#
# Требуется реализовать только эту функцию, кода вне её не должно быть.
# Функция не должна вызывать внутри себя функции input и print.
# def update_dictionary(d, key, value):
#     for i in d:
#         if isinstance(d[i],int):
#             d[i] = [d.get(i)]
#     if key in d:
#         d[key].append(value)
#     elif 2*key in d:
#         d[2*key].append(value)
#     else:
#         d.update({2 * key : [value]})
#
#
# dic = {2: 1}
# update_dictionary(dic, 1, -3)
# print(dic)
# s = 'a aa abC aa ac abc bcd a'
# def count_words(s):
#     d = {}
#     arr = s.lower().split()
#
#     for i in arr:
#         d[i] = arr.count(i)
#     for key in d:
#         print(key,d[key])
#
# count_words(s)
# ***Программа должна считывать одну строку со стандартного ввода и выводить для каждого
# уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество"
# s = input()
# d = {}
# arr = s.lower().split()
#
# for i in arr:
#     d[i] = arr.count(i)
# for key in d:
#     print(key,d[key])

# ***
# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))
# ***Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
# Далее считывает n строк с числами x_i, по одному числу в каждой строке. Итого будет n+1 строк.
# При считывании числа x_i программа должна на отдельной строке вывести значение f(x_i).
# Функция f(x) уже реализована и доступна для вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
# Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений

# n = int(input())
# s2 = []
# d = {}
# for j in range(n):
#     x = int(input())
#     if x not in s2:
#         s2.append(x)
#         d[x] = f(x)
#     print(d[x])
# ***
# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
# Sample Input:
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb

# with open('dataset_3363_2.txt') as inf:
#     s1 = inf.readline().strip()
# print(s1)
# s2 = s1[0]
# s_digits = ''
# arr = []
# for i in range(1,len(s1)):
#     if not s1[i].isdigit():
#         s2 += s1[i]
#         i += 1
#     else:
#         s_digits += s1[i]
#         if i != len(s1) -1:
#             continue
#
#     arr.append(s_digits)
#     s_digits = ''
#
# result =''
# for i in range(len(s2)):
#     result += s2[i]*int(arr[i])
# with open('file.txt','w') as ouf:
#     ouf.write(result)

# ****
# s1=''
# with open('dataset_3363_3.txt') as inf:
#     for line in inf:
#         line = line.strip()
#         s1 += line
# print(s1)
# arr =[]
# arr = s1.lower().split(' ')
# print(arr)
# d={}
# for i in arr:
#     d[i] = arr.count(i)
# print(d.values())
# ----------------------------------------
s1=''
arr =[]
with open('dataset_3363_33.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        s1+=line
arr = s1.lower().split(' ')
print(arr)

d={}
for i in arr:
    d[i] = arr.count(i)
print(d)
max = 0
s =''
for i in d:
    if d.get(i) > max:
        max = d.get(i)
        s = i
print(s, max)
# ***
# Имеется файл с данными по успеваемости абитуриентов.
# Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.
# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']
# arr=[]
# list=[]
# s =''
# middle_ab = ''
# middle_math = 0
# middle_scince = 0
# middle_lan_arts = 0
# with open('dataset_3363_4.txt') as inf:
#     for line in inf:
#         s=line.strip()
#         arr = s.split(';')
#         middle_ab += str((int(arr[1]) + int(arr[2]) + int(arr[3]))/3) + '\n'
#         with open('result.txt', 'w') as ouf:
#             ouf.write(middle_ab)
#         list.append(arr)
# print(list)
# for i in range(len(list)):
#     middle_math += int(list[i][1])/len(list)
#     middle_scince += int(list[i][2]) / len(list)
#     middle_lan_arts += int(list[i][3]) / len(list)
# total = ''
# total += str(middle_math)+ " " + str(middle_scince)+ " "  + str(middle_lan_arts)
# with open('result.txt', 'a') as ouf:
#     ouf.write(total)

# ***
# Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля,
# находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.
# import math
# r = float(input())
# print(2 * math.pi * r)

# ***
# Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран
# (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
# Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.
# Пример работы программы:
# > python3 my_solution.py arg1 arg2
# arg1 arg2

# import sys
#
# print(*sys.argv[1:])
# *******
# установка библиотек
import requests
# r = requests.get("http://exemple.com")
# print(r.text)

# url = "http://exemple.com"
# par = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(url, params=par)
# print(r.url)

# url = 'http://httpbin.org/cookies'
# cookies = {'cookies_are': 'working'}
# r = requests.get(url, cookies=cookies)
# print(r.text)
# print(r.cookies['example_cookie_name'])

# ***
# Скачайте файл.
# В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
#
# Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
#
# После получения файла вы можете проверить результат, обратившись к полю text.
# Если результат работы скрипта не принимается, проверьте поле url на правильность.
# Для подсчёта количества строк разбейте текст с помощью метода splitlines.
# В поле ответа введите одно число или отправьте файл, содержащий одно число.

# with open('dataset_3378_2.txt', 'r') as path:
#     p = path.readline().strip()
# r = requests.get(p)
# t = r.text
# s = t.splitlines()
# print(len(s))
# ***короткое решение
# with open('dataset_3378_2.txt') as inf:
#     r = requests.get(inf.readline().strip())
#     print(len(r.text.splitlines()))

# *****
# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

# base_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
# with open('dataset_3378_3.txt','r') as inf:
#     url = inf.readline().strip()
# r = requests.get(url)
#
# while not r.text.startswith("We"):
#     r = requests.get(base_url + r.text)
#
# print(r.text)


# ***через рекурсию
# import requests
#
# def req(filename):
#     r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + filename)
#     if r.text.split()[0] != 'We':
#         return req(r.text)
#     else:
#         return r.text
#
# print(req('699991.txt'))