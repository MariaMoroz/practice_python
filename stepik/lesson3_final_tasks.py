#1
# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
# d={}
# res = []
# t = 0
# total_games = [1,1]
# win = [0,0]
# draw = [0,0]
# lost = [0,0]
# total_points = [0,0]
# n = int(input())
# for i in range(n):
#     s = [j for j in input().split(';')]
#     if int(s[1]) > int(s[3]):
#         win[t] = 1
#         win[t+1] = 0
#         lost[t] = 0
#         lost[t + 1] = 1
#         total_points[t] = 3
#     elif int(s[1]) < int(s[3]):
#         lost[t] = 1
#         lost[t+1] = 0
#         win[t] = 0
#         win[t + 1] = 1
#         total_points[t+1] = 3
#     else:
#         draw[t] = 1
#         draw[t+1] = 1
#         total_points[t] = 1
#         total_points[t+1] = 1
#     for k in range(0,4,2):
#         res.append(total_games[t])
#         res.append(win[t])
#         res.append(draw[t])
#         res.append(lost[t])
#         res.append(total_points[t])
#         t += 1
#         if s[k] in d:
#             arr = d.get(s[k])
#             for i in range(len(arr)):
#                 arr[i] += res[i]
#         else:
#             d[s[k]] = res
#         res = []
#     t = 0
#     win = [0, 0]
#     draw = [0, 0]
#     lost = [0, 0]
#     total_points = [0, 0]
# for i in d:
#     print(i+':', end=' ')
#     print(*d[i])

# ***другое решение****
# n = int(input())
# teams = {}
# for i in range(n):
#     team1, goal1, team2, goal2 = input().split(';')
#
#     if team1 not in teams:
#         teams[team1] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
#
#     if team2 not in teams:
#         teams[team2] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
#
#     if goal1 > goal2:  # team1 wins
#         teams[team1]['wins'] += 1
#         teams[team1]['score'] += 3
#
#         teams[team2]['loses'] += 1
#         teams[team2]['score'] += 0
#
#     elif goal2 > goal1:  # team2 wins
#         teams[team1]['loses'] += 1
#         teams[team1]['score'] += 0
#
#         teams[team2]['wins'] += 1
#         teams[team2]['score'] += 3
#
#     elif goal1 == goal2:  # draw
#         teams[team1]['draws'] += 1
#         teams[team1]['score'] += 1
#
#         teams[team2]['draws'] += 1
#         teams[team2]['score'] += 1
#
#     teams[team1]['plays'] += 1
#     teams[team2]['plays'] += 1
# print(teams)
# for team in teams:
#     values_order = ['plays', 'wins', 'draws', 'loses', 'score']
#     print("{}:{}".format(str(team), ' '.join([str(teams[team][key]) for key in values_order])))

#2
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
# на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
# и ещё одна строка, которую нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Получаем следующие строки, которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac
# d={}
# s1_input = input()
# s2_input = input()
# s5_output =''
# s6_output =''
# def get_key(d, value):
#     for k, v in d.items():
#         if v == value:
#             return k
# if len(s1_input)==len(s2_input):
#     for i in range(len(s1_input)):
#         d[s1_input[i]]=s2_input[i]
#     s3_input = input()
#     s4_input = input()
#     for i in range(len(s3_input)):
#         s5_output += d[s3_input[i]]
#     for i in range(len(s4_input)):
#         s6_output += get_key(d, s4_input[i])
# print(s5_output)
# print(s6_output)

# ***чужок решение***
# a,b,c,d=input(),input(),input(),input()
# print(''.join(b[a.index(i)] for i in c))
# print(''.join(a[b.index(i)] for i in d))

# ***еще одно решение****
# # Считываем 4 строки в цикле
# original, coding, first_string, second_string = (input() for i in range(4))
#
# # По индексу символа из оригинала берём символ на замену из кодировки,
# # для каждого символа из строки, которую нужно закодировать
# print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# # Аналогично, только наоборот :D
# print(*[original[coding.find(symbol)] for symbol in second_string], sep='')

# ***еще одно решение****
# key, value, str1, str2 = list(input()), list(input()), list(input()), list(input())
# for i in str1:
#     print(value[key.index(i)], end = '')
# print()
# for j in str2:
#     print(key[value.index(j)], end = '')
# print()


#3
# На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках указываются эти слова.
# Затем передаётся количество l строк текста для проверки, после чего l строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
# Sample Input:
#
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
#
# Sample Output:
# stepic
# champignons
# the
# -------------------
# 3
# a
# Aa
# BCb
# 2
# A a bb aa aba ccc
# c bB aBa aba AA

# d = int(input())
# m1 = set()
# m2 = set()
# result = set()
# for i in range(d):
#     s = input().lower()
#     m1.add(s)
# l = int(input())
# for i in range(l):
#     s1 = input().lower().split(' ')
#     for j in s1:
#         m2.add(j)
# for k in m2:
#     if k.lower() not in m1:
#         result.add(k)
# print(*result, sep='\n')
#
# *****другое решение
# dic = {input().lower() for i in range(int(input()))}
#
# wrd = set()
# for w in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
#
# print(*wrd.difference(dic), sep="\n")
#
# *****другое решение
# words = set(input().lower() for i in range(int(input())))
# text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
# print('\n'.join(text - words))
# *************
#4
# start = [0,0]
# n = int(input())
# for i in range(n):
#     s = input().split(' ')
#     if s[0] == 'север':
#         start[1] += int(s[1])
#     elif s[0] == 'восток':
#         start[0] += int(s[1])
#     elif s[0] == 'юг':
#         start[1] -= int(s[1])
#     elif s[0] == 'запад':
#         start[0] -= int(s[1])
# print(*start)
# *****другое решение
# n=int(input())
# d={'север':0,'запад':0,'юг':0,'восток':0}
# for i in range(n):
#     x=input().split()
#     d[x[0]]+=int(x[1])
# print(d['восток']-d['запад'], d['север']-d['юг'])
# ****************
# 5
#
# d={}
# k=[]
# with open('dataset_3380_5.txt', 'r') as inf:
#     for line in inf:
#         s = line.strip().split()
#         if int(s[0]) not in d:
#             d[int(s[0])] = [s[1], int(s[2])]
#         else:
#             d[int(s[0])] +=[s[1], int(s[2])]
#     print(d)
# sum=0
# res={}
# count = 0
# for i in d:
#     for j in range(len(d[i])):
#         if isinstance(d[i][j], int):
#             count+=1
#             sum += d[i][j]
#     res[i] = sum/count
#     count = 0
#     sum=0
# for k in sorted(res.keys()):
#     print(k, ' ', res[k])
import math
print(str(math.ceil(math.pow(math.pi, math.e)*10000)))