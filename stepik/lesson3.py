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
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
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






