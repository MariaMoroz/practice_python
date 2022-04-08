# 5.0
#     1) Write a function to compare 2 numbers.
# 	E.g. compare(2, 3) should return False otherwise should return True.

# def compare_numbers(a,b):
#     return a > b
# print(compare_numbers(4,3))
# ***************************************
# def compare_input_numbers():
#     a = int(input())
#     b = int(input())
#     return a > b
# print(compare_input_numbers())

#
#     2) Modify the previous function to compare only positive numbers.
# 	In case of negative numbers it will return a print statement like: "Can compare only positive numbers!".
#
# def compare_input_positive_numbers():
#     a = int(input())
#     b = int(input())
#     if a < 0 or b < 0:
#         return "Can compare only positive numbers!"
#     else:
#         return a > b
# print(compare_input_positive_numbers())

#     3) Write a function to sum 2 numbers.
# 	E.g. add(4, 5) should return 9 as a result.
#
# def sum_input_numbers():
#     a = int(input())
#     b = int(input())
#     return a + b
# print(sum_input_numbers())

#     4) Write a function to subtract 2 numbers.
# 	E.g. sub(4, 2) should return 2 as a result.
#
# def sub_input_numbers():
#     a = int(input())
#     b = int(input())
#     return a - b
# print(sub_input_numbers())

#     5) Write a function that returns a type of input.
# 	E.g. give_a_type("test") should return a print statement like: "string".

# def give_a_type(s):
#
#     if isinstance(s, str):
#         return "string"
#     elif isinstance(s, int):
#         return "integer"
# print(give_a_type(5))
# print(give_a_type('5'))

# 6) Write a function that prints input vertically.
# 	E.g. print_vertical("test me please") should return:
# t
# e
# s
# t
#
# m
# e
#
# p
# l
# e
# a
# s
# e
# def print_vertical():
#     s = input()
#     for i in s:
#         print(i)
# print_vertical()

# 7) Write a function that concatenates 2 strings.
# 	E.g. concat("abc" , "123") should return a print statement like: "adc123".
# def concat():
#     s1 = input()
#     s2 = input()
#     return s1+s2
# print(concat())