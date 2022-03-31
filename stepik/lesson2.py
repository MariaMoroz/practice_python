# for n in range(5, 57, 2):
#     print(n)
# ******
# i = 0
# count = 0
# while i <= 10:
#     i = i + 1
#     count+=1
#     if i > 7:
#         i = i + 2
# print(count)
# *****
# n = int(input())
# for i in range(1, n):
#     print('*'*i)
# ******
# n = int(input())
# stars = '*'
# while len(stars) <= n:
#     print(stars)
#     stars += '*'
# ****
# sum = 0
# for i in range(3,8):
#     sum += i
# print(sum)
# ****
# sum = 0
# i = 1
# while i != 0:
#     n = int(input())
#     sum += n
#     i = n
# print(sum)
# ***НОК
# a = int(input())
# b = int(input())
# num_1 = a
# num_2 = b
# if a > b:
#     a, b = b, a
# while b != 0:
#     a, b = b, a % b
# nod = a
# nok = (num_1 * num_2)// nod
# print(nok)
# ***
# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
#
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
# a = 1
# arr = []
# while a <= 100:
#     a = int(input())
#
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     else:
#         arr.append(a)
#
# for i in range(len(arr)):
#     print(arr[i])
# другое решение
# while True:
#     number = int(input())
#     if number >100:
#         break
#     if number <10:
#         continue
#     print(number)
# ****
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*  ', end = '')
#     print()
# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
# Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
# Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# len_colmn = b - a + 1
# len_row = d - c + 1
# arr_colmn = []
# arr_row = []
# for i in range(len_colmn):
#     arr_colmn.append(a + i)
# for j in range(len_row):
#     arr_row.append(c + j)
#
# for i in range(len_row):
#     print('\t', arr_row[i], end ='')
# print()
# for i in range(len_colmn):
#     print(arr_colmn[i],end='')
#     for j in range(len_row):
#         print('\t', arr_colmn[i]*arr_row[j], end='')
#     print()
# print()
# ***другое решение****
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# for i in range(c, d + 1):
#     print("\t" + str(i), end="")
# print()
#
# for i in range(a, b + 1):
#     print(i, end="\t")
#     for n in range(c, d + 1):
#         print(i * n, end="\t")
#     print()
# ***найти сумму всех нечетных чисел в заданном интервале [a,b]
# a = int(input())
# b = int(input())
# sum = 0
# for i in range(a, b + 1):
#     if i % 2 == 1:
#         sum += i
# print(sum)
# ***второе решение*****
# a = int(input())
# b = int(input())
# sum = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     sum += i
# print(sum)
# ****
# a, b = input().split()
# print(a, b)
# Напишите программу, которая считывает с клавиатуры два числа aa и bb,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b], которые кратны числу 3.
# a, b = input().split()
# a = int(a)
# b = int(b)
# sum = 0
# count = 0
# res = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         sum += i
#         count +=1
# res = sum / count
# print(res)
# ***Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов).
# stroka = input()
# count_C = stroka.upper().count('C')
# count_G = stroka.upper().count('G')
# print(((count_C + count_G) / len(stroka)) * 100)
# ***
# s = "abcdefghijk"
# print(s[:-6])
# print(s[-1:-10:-2])
# *****
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
# то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

# s = input()
# new_s = s[0]
# count = 1
# for i in range(0, len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         new_s += str(count)
#         new_s += s[i+1]
#         count = 1
# print(new_s + str(count))

# ****Списки*****
# students = ['Ivan', 'Masha', 'Sasha', 'Masha']
# # students += ['Olga']
# students += 'Olga'
# students.remove('Masha')
# print(students)
# a = [1, 2, 3]
# b = a
# print(b)
# a[1] = 10
# print(b)
# b[0] = 20
# print(a)
# a = [5, 6]
# print(b)
# print(a)
# print(a*3)
# ***
# Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел.
# Используйте метод split строки.
# sum = 0
# arr = [int(i) for i in input().split()]
# for i in arr:
#     sum += i
# print(sum)

# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# arr = [int(i) for i in input().split()]
# last_ind = len(arr)
# new_arr = [arr[i] for i in range(last_ind)]
# if len(arr) == 1:
#     new_arr = arr
# else:
#     for i in range(0, last_ind):
#         if i == 0:
#             new_arr[i] = arr[i+1] + arr[last_ind - 1]
#         elif i == last_ind - 1:
#             new_arr[i] = arr[i - 1] + arr[0]
#         else:
#             new_arr[i] = arr[i + 1] + arr[i - 1]
# for i in new_arr:
#     print(i, end =' ')
# ***другое решение***
# numbers = [int(i) for i in input().split()]
# if len(numbers) == 1:
#     print(numbers[0])
# else:
#     for i in range(len(numbers)):
#         print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")
#         # print(i, (i + 1) % len(numbers), end=" ")
#         # print()
# ***
# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза.
# numbers, res = [str(i) for i in input().split()], []
# numbers = [i for i in input().split()]
# res = []
# for i in numbers:
#     if numbers.count(i) > 1 and i not in res:
#         res.append(i)
#         print(i, end = ' ')
# ***двумерные списки********
# n = 3
# a = [[0]*n for i in range(n)]
# print(a)
# b = [[0 for j in range(n)] for i in range(n)]
# print(b)

# ****игра сапер****
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1
# print(a) [[-1, 0, 0, 0], [0, -1, 0, 0], [0, -1, 0, 0], [0, 0, 0, -1], [0, 0, 0, 0]]
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] +=1
# print(a) [[-1, 2, 1, 0], [3, -1, 2, 0], [2, -1, 3, 1], [1, 1, 2, -1], [0, 0, 1, 1]]

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()