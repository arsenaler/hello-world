# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class GatewayAddport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.8.42.2/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_gateway_addport(self):
        driver = self.driver
        driver.get(self.base_url + "/dashboard/auth/login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_css_selector("dt > div").click()
        driver.find_element_by_xpath("//div[@id='main_content']/div[2]/div/dl/dd/div[2]/h4").click()
        driver.find_element_by_link_text(u"路由").click()
        driver.find_element_by_id("Routers__action_create").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("testtest2")
        driver.find_element_by_xpath(u"//input[@value='新建路由']").click()
        driver.find_element_by_css_selector("a[id$=\"setgateway\"]").click()
        Select(driver.find_element_by_id("id_network_id")).select_by_visible_text("net04_ext")
        driver.find_element_by_css_selector("option[value=\"f4f56079-84e1-41ac-bc5d-ebeef5699220\"]").click()
        driver.find_element_by_xpath(u"//input[@value='设置网关']").click()
        time.sleep(2)
        driver.find_element_by_link_text("testtest2").click()
        driver.find_element_by_id("interfaces__action_create").click()
        Select(driver.find_element_by_id("id_subnet_id")).select_by_visible_text("test2: 2.1.1.0/24 (test2)")
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='add_interface_form']/div[2]/input").click()

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
