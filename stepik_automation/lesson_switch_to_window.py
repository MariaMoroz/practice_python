import math
from selenium import webdriver
import time


try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element_by_css_selector("button[type='submit']")
    button_1.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    el_input = browser.find_element_by_id('answer')
    el_input.send_keys(y)

    button_2 = browser.find_element_by_xpath("//button[text()='Submit']")
    button_2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()