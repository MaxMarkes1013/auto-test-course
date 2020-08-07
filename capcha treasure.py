from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    place = browser.find_element_by_css_selector("[src='images/chest.png']")
    value1 = place.get_attribute("valuex")
    x = value1

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