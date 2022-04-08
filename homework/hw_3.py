# Lesson 3
#
#     1) Write a program to return a boolean value as a print statement if one number is greater than another.
#        E.g. If X is greater than Y return True otherwise return False
#
#     2) Modify the previous program to return a string value as a print statement like:
# 	"10 is greater than 5" Or opposed "2 is less than 4"
#
#     3) Modify the previous program to cover the case to compare only positive numbers, zero is not included!
# 	in case one of the variables is zero return a string value as a print statement like:
# 	"One or both numbers are not positive, can't proceed with the comparison!"
a = 5
b = 0
# if a > b:
#     print(True)
# else:
#     print(False)
# # 2
# if a > b:
#     print(f'{a} is greater than {b}')
# else:
#     print(False)

# 3
if a > 0 and b > 0:
    if a > b:
        print(f'{a} is greater than {b}')
    print(False)
else:
    print("One or both numbers are not positive, can't proceed with the comparison!")

