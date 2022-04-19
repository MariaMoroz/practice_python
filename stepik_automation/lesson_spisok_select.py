from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el_num_1 = browser.find_element_by_id('num1').text
    el_num_2 = browser.find_element_by_id('num2').text
    num_1 = int(el_num_1)
    num_2 = int(el_num_2)
    sum = num_1 + num_2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

