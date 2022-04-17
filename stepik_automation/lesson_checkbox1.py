import math
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

el_input = browser.find_element_by_id('answer')
el_input.send_keys(y)

el_checkbox = browser.find_element_by_id('robotCheckbox')
el_checkbox.click()

el_radiobtn = browser.find_element_by_id('robotsRule')
el_radiobtn.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()