# lst = [5, 2, 6]
# lst.append(17)
# print(lst)
# lst.pop()
# print(lst)
# lst.pop(0)
# print(lst)
# lst.insert(0, 5)
# print(lst)
# lst.insert(1, 'Muffin')
# print(lst)
# lst.append([25,50])
# print(lst)
# lst.insert(0, [6,'apple'])
# print(lst)
# lst.insert(-1, ('book', 'magazin'))
# print(lst)
# print(lst[-1])
# print(lst[1])

# my_list = [3, 5, 2, 4, 3, 2]
# s = set(my_list)
# if len(s) == len(my_list):
#     print("Элементы уникальны")
# else:
#     print("Не уникальны")
d = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    1: 34,
    2: [9,14]
}
d['new key'] = 2
print(d)
d[('new_tuple_key',)] = [4,3,'lll']
print(d)
print(d.get('key1'))
del d['key1']
print(d)
d.pop(('new_tuple_key',))
print(d)
print(d.keys())
