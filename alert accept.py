from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(1)

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    place = browser.find_element_by_id("input_value")
    x = place.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y=calc(x)

    result = browser.find_element_by_id("answer")
    result.send_keys(y)
    time.sleep(1)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
