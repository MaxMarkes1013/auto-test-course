from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element_by_xpath("/html/body/div/form/div/label/span[@id='input_value']")
    x = value1.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y=calc(x)

    result = browser.find_element_by_id("answer")
    result.send_keys(y)
    time.sleep(1)

    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()
    time.sleep(1)

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    time.sleep(1)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:

    time.sleep(10)
    browser.quit()