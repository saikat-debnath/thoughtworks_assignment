from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Flow_2 (unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.driver.get("https://www.flipkart.com/")

    def tearDown(self):
        self.driver.quit()

    def test__product_search(self):
        close_icon_in_login_popup = self.driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
        close_icon_in_login_popup.click()
        click_on_loginandsignup_text = self.driver.find_element_by_xpath("//a[contains(text(),'Login & Signup')]")
        click_on_loginandsignup_text.click()
        time.sleep(5)
        email_text_box = self.driver.find_element_by_xpath("//div[@class='_39M2dM']//input[@type='text']")
        email_text_box.send_keys("debnath.saikat76@gmail.com")
        pwd_text_box = self.driver.find_element_by_xpath("//input[@type='password']")
        pwd_text_box.send_keys("abcdefgh")
        login_button = self.driver.find_element_by_xpath("//button[@type='submit']//span[contains(text(),'Login')]")
        login_button.click()
        search_text_box = self.driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']")
        search_text_box.click()
        search_text_box.send_keys("macbook air")
        search_text_box.send_keys(u'\ue007')
        click_on_product = self.driver.find_element_by_xpath("//a[@title='Apple MacBook Air Core i5 5th Gen - (8 GB/128 GB SSD/Mac OS Sierra) MQD32HN/A A1466']")
        click_on_product.click()
        multiple_window_id = self.driver.window_handles
        parent_window_id = multiple_window_id[0]
        child_window_id = multiple_window_id[1]
        switch_to_child_window = self.driver.switch_to.window(child_window_id)
        time.sleep(5)

