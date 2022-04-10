# 6.0
#
#    1) Write a program/function that prints list entities one by one. As an input use a list.
# 	e.g. print_entities(["a", "b", "c"]) should return:
# 		"a"
# 		"b"
# 		"c"
#
# def print_list():
#     arr = [i for i in input().split()]
#     for j in arr:
#         print(j)
# print_list()

#    2) Write a program/function that converts strings into tuples.
# 	e.g. convert("abide") should return tuple like:
# 		("a", "b", "i", "d", "e")
#
# def convert():
#     s = input()
#     t = set()
#     for i in s:
#         t.add(i)
#     return t
# print(convert())


#    3) Write a program/function that removes duplicates and returns only unique values as a list.
# 	e.g. remove_dups("abcdadab") should return ["a", "d", "c", "b"]. Note, order of elements in the list is not important!
#
# def convert():
#     arr=[]
#     s = input()
#     t = set()
#     for i in s:
#         t.add(i)
#     for i in t:
#         arr.append(i)
#     return arr
# print(convert())
#    4) Write a program/function that collects certain data as parameters and returns a dictionary object.
# 	e.g. client("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261") should return a dictionary object like:
# 		{
# 			"Name": "John",
# 			"Lastname": "Doe",
# 			"DOB": "01/23/1934",
# 			"Sex": "Male",
# 			"City": "San Antonio",
# 			"State": "TX",
# 			"ZipCode": "78261"
# 		}
def client(data):
    key = ['name', 'lastname', 'DOB', 'sex', 'city', 'state', 'Zipcode']
    d = {}
    for i in range(len(key)):
        d[key[i]] = data[i]
    return d
print(client(["John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261"]))