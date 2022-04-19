import os
from selenium import webdriver
import time

# пример
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)

print(os.path.abspath(__file__)) #результат - D:\school\projectPython\stepik_automation\lesson_work_with_files.py
print(os.path.abspath(os.path.dirname(__file__))) #D:\school\projectPython\stepik_automation

# В этом задании в форме регистрации требуется загрузить текстовый файл.


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Ivan@ivanov.com")

    btn_file = browser.find_element_by_id('file')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    btn_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
