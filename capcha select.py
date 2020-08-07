from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text

    summ = int(number1) + int(number2)
    sumstr = str(summ)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sumstr)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:

    time.sleep(10)
    browser.quit()
