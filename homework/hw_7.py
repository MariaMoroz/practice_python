# 7.1 Create a program/function that gets a parameter as a text,
#     creates file "text.txt" and inserts the text into the file.
#     As the result of the program/function, we have to get our file "text.txt"
#     with the content from the parameter.
# """
def get_text(text):
    with open("text.txt", "w") as a:
        a.write(text)
    with open("text.txt", "r") as inf:
        s = inf.read()
    return s

print(get_text('*******************************'))


# 7.2 Create a program/function that gets 2 parameters,
#     first parameter a file name,
#     second parameter character (letter, number)
#     and replaces all characters in the file to 0 which equals the second parameter.
#     E.g. we have a file "my_text.txt" with the text "Hello Python! Lesson 7",
#     we pass the second parameter as "e" to the program/function, and as the result
#     text in the file will be "H0llo Python! L0sson7"

def replace_letters(name, letter):
    with open(name,'r') as inf:
        s = inf.read()
    result = ''
    # result=s.replace(letter,'0')
    for i in s:
        if i == letter:
            result += '0'
        else:
            result += i

    return result

print(replace_letters("replace_text.txt",'e'))