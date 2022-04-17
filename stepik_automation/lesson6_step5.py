import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    el = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    # //div/a[text() = '224592']
    sel = '//div/a[text()=' + el + ']'
    element = browser.find_element_by_xpath(sel)
    element.click()

    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

