from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

button = browser.find_element_by_id("book")

text = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

value1 = browser.find_element_by_id("input_value")
x = value1.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y=calc(x)

result = browser.find_element_by_id("answer")
result.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()
time.sleep(5)
