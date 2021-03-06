from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    ecpected_text = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element_by_id("book")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    el_input = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", el_input)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    el_input.send_keys(y)

    button_2 = browser.find_element_by_xpath("//button[text()='Submit']")
    button_2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()