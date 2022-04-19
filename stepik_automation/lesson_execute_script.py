from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    el_input = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", el_input)

    el_input = browser.find_element_by_id('answer')
    el_input.send_keys(y)

    el_checkbox = browser.find_element_by_id('robotCheckbox')
    el_checkbox.click()

    el_radiobtn = browser.find_element_by_id('robotsRule')
    el_radiobtn.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()