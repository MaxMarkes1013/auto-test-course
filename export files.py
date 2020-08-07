from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    field1 = browser.find_element_by_name("firstname")
    field1.send_keys("Max")
    time.sleep(0.5)

    field2 = browser.find_element_by_name("lastname")
    field2.send_keys("Markes")
    time.sleep(0.5)

    field3 = browser.find_element_by_name("email")
    field3.send_keys("trial@mail.com")
    time.sleep(0.5)
    
    current_dir = os.path.abspath(os.path.dirname("C:\\Users\\Max\\selenium_course\\"))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    button = browser.find_element_by_name("file")
    button.send_keys(file_path)
    time.sleep(0.5)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
