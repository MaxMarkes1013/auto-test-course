from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

try:
    find1 = browser.find_element_by_link_text("224592")
    time.sleep(3)
    find1.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    time.sleep(0.5)
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    time.sleep(0.5)
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    time.sleep(0.5)
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    time.sleep(0.5)
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
