from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    place = browser.find_element_by_id("input_value")
    x = place.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y=calc(x)

    result = browser.find_element_by_id("answer")
    result.send_keys(y)
    time.sleep(1)
    
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
