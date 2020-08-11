from selenium import webdriver
import unittest

class TestCase1(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)

        field1 = self.browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        field1.send_keys("Max")

        field2 = self.browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        field2.send_keys("Markes")

        field3 = self.browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        field3.send_keys("markes@max.com")

        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)

        field1 = self.browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        field1.send_keys("Max")

        field2 = self.browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        field2.send_keys("Markes")

        field3 = self.browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        field3.send_keys("markes@max.com")

        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        
    def tearDown(self):
        self.browser.quit()

         

if __name__ == "__main__":
    unittest.main()

