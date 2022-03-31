# N1
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)
# N2
# n = int(input())
# if n > -15 and n <=12 or n > 14 and n < 17 or n >= 19:
#     print(True)
# else:
#     print(False)
# 3 калькулятор
# a = float(input())
# b = float(input())
# op = input()
# if op == '+':
#     print(a + b)
# if op == '-':
#     print(a - b)
# if op == '*':
#     print(a * b)
# if op == '/' and b != 0:
#     print(a / b)
# elif op == '/' and b == 0:
#     print("Деление на 0!")
# if op == 'mod' and b != 0:
#     print(a % b)
# elif op == 'mod' and b == 0:
#     print("Деление на 0!")
# if op == 'pow':
#     print(a ** b)
# if op == 'div' and b != 0:
#     print(a // b)
# elif op == 'div' and b == 0:
#     print("Деление на 0!")
# другое решение
# a = float(input())
# b = float(input())
# act = input()
#
# if (act=="/" or act=="mod" or act=="div") and b==0:
#     c = "Деление на 0!"
# elif act=="+":    c = a + b
# elif act=="-":    c = a - b
# elif act=="/":    c = a / b
# elif act=="*":    c = a * b
# elif act=="mod":  c = a % b
# elif act=="pow":  c = a ** b
# elif act=="div":  c = a // b
#
# print (c)
# 4
# n = input()
# if n == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# elif n =='прямоугольник':
#     a = int(input())
#     b = int(input())
#     S = a * b
# elif n == 'круг':
#     r = int(input())
#     S = 3.14 * r * r
# print(float(S))
# 5
# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c and b >= c:
#     max_num = a
#     min_num = c
#     num = b
# if a >= b and a >= c and c >= b:
#     max_num = a
#     min_num = b
#     num = c
# if b >=c and b >= a and a >= c:
#     max_num = b
#     min_num = c
#     num = a
# if b >=c and b >= a and c >= a:
#     max_num = b
#     min_num = a
#     num = c
# if c >= b and c >= a and a >= b:
#     max_num = c
#     min_num = b
#     num = a
# if c >= b and c >= a and b >= a:
#     max_num = c
#     min_num = a
#     num = b
# print(max_num, min_num, num, sep='\n')
# 5 other way
# a,b,c = int(input()),int(input()),int(input())
# max = a
# min = a
# if b > max: max = b
# if c > max: max = c
# if b < min: min = b
# if c < min: min = c
# mid = (a + b + c) - (max + min)
# print(max)
# print(min)
# print(mid)
# 6
# n = int(input())
# for n in range(1001):
#     word = 'программист'
#     if n % 10 == 1 and n != 11 and ((n % 100) // 10 != 1):
#         print(f'{n} {word}')
#     elif (n % 10 == 2 or n % 10 == 3 or n % 10 == 4) and (n < 5 or n > 20) and ((n % 100) // 10 != 1):
#         print(f'{n} {word}а')
#     else:
#         print(f'{n} {word}ов')
# другое решение
# n = int(input())
# d = n % 10
# h = n % 100
# if d == 1 and h != 11:
#     s = ""
# elif 1 < d < 5 and not 11 < h < 15:
#     s = "а"
# else:
#     s = "ов"
# print(n, "программист" + s)
# 7
# num = input()
# sum_1 = 0
# sum_2 = 0
# for i in range(6):
#     if i < 3:
#         sum_1 += int(num[i])
#     else:
#         sum_2 += int(num[i])
# if sum_1 == sum_2:
#     print("Счастливый")
# else:
#     print("Обычный")