# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
# a = int(input())
# sum = a
# sum_result = a**2
# while sum != 0:
#     a = int(input())
#     sum += a
#     sum_result += a**2
# print(sum_result)

# ***
# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно).
# На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
# n = int(input())
# num = 1
# stroka = ''
# arr = []
# while len(arr) < n:
#     for i in range(1, num + 1):
#         if len(arr) < n:
#             arr.append(num)
#         else: break
#     num += 1
# print(*arr)
# *****лучшее решение*****
# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])
# *****
# Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки,
# которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
# Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует"
# n = [int(i) for i in input().split()]
# x = int(input())
# flag = 0
# for i in range(len(n)):
#     if n[i] == x:
#         print(i, end = ' ')
#         flag = 1
# if flag == 0:
#     print("Отсутствует")

# ***
# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
# После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы
# на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

# n = input().split()
# row = len(n)
# arr = []
# arr.append(n)
# while n != ['end']:
#     n = input().split()
#     if n !=['end']:
#         arr.append(n)
# l = len(arr)
#
# if l == 1 and row == 1:
#     el = int(arr[0][0])
#     print(el * 4)
# else:
#     for i in range(len(arr)):
#         for j in range(row):
#             sum = int(arr[i-1][j]) + int(arr[(i+1)%len(arr)][j]) + int(arr[i][j-1]) + int(arr[i][(j+1)%row])
#             print(sum, end=' ')
#         print()
#
# ***другое решение
# c = []
# while True:
#     a = [i for i in input().split()]
#     if a == ['end']:
#         break
#     c.append(a)
# n, m = len(c), len(c[0])
# for i in range(n):
#     for j in range(m):
#         x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
#         print(x, end=' ')
#     print()
# **********
# Выведите таблицу размером n×n, заполненную числами от 1 до n^2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке:
# n = int(input())
# mat = [[0]*n for i in range(n)]
# st, m = 1, 0
# # Заранее присваиваю значение центральному элементу
# # матрицы
# mat[n//2][n//2]=n*n
# for v in range(n//2):
#     #Заполнение верхней горизонтальной матрицы
#     for i in range(n-m):
#         mat[v][i+v] = st
#         st+=1
#         #i+=1
#     #Заполнение правой вертикальной матрицы
#     for i in range(v+1, n-v):
#         mat[i][-v-1] = st
#         st+=1
#         #i+=1
#     #Заполнение нижней горизонтальной матрицы
#     for i in range(v+1, n-v):
#         mat[-v-1][-i-1] =st
#         st+=1
#         #i+=1
#     #Заполнение левой вертикальной матрицы
#     for i in range(v+1, n-(v+1)):
#         mat[-i-1][v]=st
#         st+=1
#         #i+=1
#     #v+=1
#     m+=2
# #Вывод результата на экран
# for i in mat:
#     print(*i)

# ***
# n=int(input())
# t=[[0]*n for i in range (n)]
# i,j=0,0
# for k in range(1, n*n+1):
#   t[i][j]=k
#   if k==n*n: break
#   if i<=j+1 and i+j<n-1: j+=1
#   elif i<j and i+j>=n-1: i+=1
#   elif i>=j and i+j>n-1: j-=1
#   elif i>j+1 and i+j<=n-1: i-=1
# for i in range(n):
#   print(*t[i])

# ***Решение через заполнение матрицы из середины.
n = int(input())**2
mx = [[]]
while n > 0:
    row_count = len(mx)
    for i in range(row_count):
        mx[i].insert(0, n)
        n -= 1
    mx = [[*x] for x in zip(*mx[::-1])]
for row in mx:
    print(*row)
# *********
# n = ['el1','el2', 2]
# for i in n:
#     if isinstance(i, int):
#         print('number is ', i)
