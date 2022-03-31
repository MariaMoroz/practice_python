import string

s = string.ascii_lowercase
print(s)
for i in range(1, 11):
    print(i,s[i-1])

# s = list(string.ascii_lowercase[:10])
# for i in range(11):
#     print(i,s[i-1])