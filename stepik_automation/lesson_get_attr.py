from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
el_picture = browser.find_element_by_id('treasure')
x = el_picture.get_attribute('valuex')
y = calc(x)
el_input = browser.find_element_by_id('answer')
el_input.send_keys(y)
el_checkbox = browser.find_element_by_id('robotCheckbox')
el_checkbox.click()
el_radiobtn = browser.find_element_by_id('robotsRule')
el_radiobtn.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()