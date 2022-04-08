# Lesson4
#
# 4.0
# 1) Write a program to print result like(use loop):
# H
# e
# l
# l
# o
#
# P
# y
# t
# h
# o
# n
# !
s = 'Hello Python!'
for i in s:
    print(i)


# 4.1
# 1) Write a program that uses a loop and prints numbers from 1 to 100 but the program should stop
# if a number is equal to 45.
for i in range(1, 101):
    if i != 46:
        print(i)
    else:
        break


#
# 4.2
# 1) Write a program that prints even numbers from 1 to 20.
for i in range(2,21,2):
    print(i, end=' ')
print()
# 2) Write a program that prints odd numbers from 1 to 30.
for i in range(1,30,2):
    print(i, end=' ')
print()
# 4.3
# 1) Write a program that prints first 10 letters from ABC, the results should be like:
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 6 f
# 7 g
# 8 h
# 9 i
# 10 j
#
s = 'abcdefghijklmnopqrstuvwxyz'
i=1;
while i != 11:
    print(i, s[i-1])
    i+=1
# 4.4
# 1) Write a program that prints numbers from 30 to 0 in decreasing order.
for i in range(30,-1,-1):
    print(i)

