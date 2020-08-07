from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    placeX = browser.find_element_by_id("input_value")
    x = placeX.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    result = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(result)
    time.sleep(0.5)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 120);")
    time.sleep(0.5)

    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()
    time.sleep(0.5)

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    time.sleep(0.5)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()