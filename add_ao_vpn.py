# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from bs4 import BeautifulSoup
import os
import hashlib
import re
from html2text import html2text
import thread
import threading
import SendKeys
import win32con
import win32gui
from bs4 import BeautifulSoup



def switch_to_default_window(driver):
        all_handles = driver.window_handles
        current_handle = driver.current_window_handle
        for handle in all_handles:
            if handle != current_handle:
                driver.switch_to.window(handle)
class login(object):
    Address_Objects = (By.LINK_TEXT,"Address Objects")

    def __init__(self):
        self.driver = webdriver.Firefox()

    '''
    def switch_to_default_window(cls):


		cls.driver.switch_to.default_content()
		all_handle = cls.driver.window_handles
		current_handle = cls.driver.current_window_handle
		for handle in all_handle:
			if handle != current_handle:
				cls.driver.switch_to.window(handle)
    '''

    def login_web(self):
        base_url = self.base_url = "https://10.8.43.60/"
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
#        base_url = "http://10.8.42.2/"
        driver.get(base_url + "auth.html")
#    driver.switch_to.window("SonicWall Administrator")
        driver.switch_to.frame("authFrm")
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("admin")
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("password")
        driver.find_element_by_name("Submit").click()


    def logout(self):
        self.driver.quit()

    def switch_to_Network(self):
        driver = self.driver
        driver.switch_to.default_content()
        driver.switch_to.frame("outlookFrame")
        driver.find_element_by_link_text("Network").click()
#        address_objects = self.driver.find_element('Network')
#        driver.execute_script("arguments[0].click();", address_objects)
        time.sleep(2)

    def switch_to_vpn(self):
        driver = self.driver
        driver.switch_to.default_content()
        driver.switch_to.frame("outlookFrame")
        driver.find_element_by_link_text("VPN").click()

    def switch_to_settings(self):
        driver = self.driver
        driver.switch_to.default_content()
        driver.switch_to.frame('outlookFrame')
        button = driver.find_element_by_link_text('Settings')
        driver.execute_script("arguments[0].click();", button)
        time.sleep(4)

    def switch_to_firewall_Settings(self):
        driver = self.driver
        driver.switch_to.default_content()
        driver.switch_to.frame('outlookFrame')
        button = driver.find_element_by_link_text('Firewall Settings')
        driver.execute_script('arguments[0].click()', button)
        time.sleep(2)

    def switch_to_default_window(self):
        driver = self.driver
        all_handles = driver.window_handles
        current_handle = driver.current_window_handle
        for handle in all_handles:
            if handle != current_handle:
                driver.switch_to.window(handle)

    def switch_window(self, windowname):
        driver = self.driver
        driver.maximize_window()
        driver.switch_to.default_content()
        all_handles = driver.window_handles
        for handle in all_handles:
            driver.switch_to.window(handle)
            if driver.title == windowname:
                driver.switch_to.window(handle)
                break
        print driver.title

    def test_add_ao(self):
        driver = self.driver
        driver.switch_to.default_content()
        self.switch_to_Network()
        driver.find_element_by_link_text("Address Objects").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame("tabFrame")
        time.sleep(2)
        button = driver.find_element_by_id("addAoBtn")
        driver.execute_script("arguments[0].click();", button)
       # driver.find_element_by_id("addAoBtn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | 10_8_42_58_addrObjdlg | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=10_8_42_58_addrObjdlg | ]]
        time.sleep(2)
#        driver.switch_to.window("Add Address Object")
        self.switch_window("Add Address Object")
        driver.find_element_by_name('noName').clear()
        driver.find_element_by_name('noName').send_keys('testvsss58668')
        Select(driver.find_element_by_name("zone")).select_by_visible_text("LAN")
        Select(driver.find_element_by_name("noType")).select_by_visible_text("Range")
        driver.find_element_by_id("noIp1").clear()
        driver.find_element_by_id("noIp1").send_keys("9.9.9.9")
        driver.find_element_by_id("noIp2").clear()
        driver.find_element_by_id("noIp2").send_keys("9.9.9.99")
        button = driver.find_element_by_id("actionBtn0")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        driver.find_element_by_name('noName').clear()
        driver.find_element_by_name('noName').send_keys('testvsss5668')
        '''
        Select(driver.find_element_by_name("zone")).select_by_visible_text("VPN")
        Select(driver.find_element_by_name("noType")).select_by_visible_text("Range")
        '''
        driver.find_element_by_name('noType').find_element_by_xpath("//option[@value='VPN']").click()
        Select(driver.find_element_by_name("noType")).select_by_visible_text("Range")
        select = driver.find_element_by_tag_name('select')
        all_options = select.find_elements_by_tag_name('option')
        for option in all_options:
            print option
        driver.find_element_by_id("noIp1").clear()
        driver.find_element_by_id("noIp1").send_keys("99.99.9.9")
        driver.find_element_by_id("noIp2").clear()
        driver.find_element_by_id("noIp2").send_keys("99.99.9.99")
        button = driver.find_element_by_id("actionBtn0")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)



        button1 = driver.find_element_by_id("closeBtn0")
        driver.execute_script("arguments[0].click();", button1)
        print driver.current_url
        driver.close()
        driver.refresh()


      #  self.switch_to_default_window()
        driver.switch_to.default_content()
        print driver.title
        handles = driver.window_handles
        handle1 = driver.current_window_handle
        print handles[1]
        print len(handles)
        print handle1
        for handle in handles:
            print 'test'
            if handle != handle1:
                driver.switch_to.window(handle)
                print driver.title
            else:
                driver.find_element_by_id("closeBtn0").click()








    def add_vpn_policy(self):
        print 'test.dsdafas'
        driver = self.driver
        driver.switch_to.default_content()
        self.switch_to_vpn()
        print 'testdds'
#        driver.find_element_by_link_text("Settings").click()
        driver.switch_to.default_content()
        driver.switch_to.frame("tabFrame")
        time.sleep(2)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=tabFrame | ]]
        button = driver.find_element_by_name("addVpnPolBtn")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        self.switch_window("VPN Policy")

        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | 10_8_42_58_dialogScroll | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=10_8_42_58_dialogScroll | ]]
    #    driver.find_element_by_id("t1Label").click()
        driver.find_element_by_id("ipsecName").clear()
        driver.find_element_by_id("ipsecName").send_keys('vpn_policy_s2s')
        driver.find_element_by_id("ipsecGwAddr").clear()
        driver.find_element_by_id("ipsecGwAddr").send_keys('10.8.42.24')
        driver.find_element_by_id("ipsecIkePskCtl").clear()
        driver.find_element_by_id('ipsecIkePskCtl').send_keys('111111')
        driver.find_element_by_id('confirmPsk').clear()
        driver.find_element_by_id('confirmPsk').send_keys('111111')
        driver.find_element_by_id("t1Label").click()
        Select(driver.find_element_by_name("ipsecLocalNetwork")).select_by_visible_text("testvsss58668")
        Select(driver.find_element_by_name("ipsecRemoteNetwork")).select_by_visible_text("testvsss5668")


        driver.find_element_by_id("t2Label").click()

        driver.find_element_by_id("t3Label").click()
        driver.find_element_by_id("ipsecKeepAlive").click()
        driver.find_element_by_id("ipsecHttpsUsrLogin").click()
        driver.find_element_by_id("ipsecHttpsMgmt").click()
        driver.find_element_by_name("ok").click()
        time.sleep(3)
        print 'dddddaaaaaaaaaaaadddddd'
        handles = driver.window_handles
        handle1 = driver.current_window_handle
#        switch_to_default_window(driver)
        for handle in handles:
            driver.switch_to.window(handle)
            if handle != handle1:
                driver.switch_to.window(handle)
        print driver.title

    def test_upload_firmware(self):
        driver = self.driver
        self.switch_to_settings()

        driver.switch_to.default_content()
        driver.switch_to.frame("tabFrame")
        driver.find_element_by_xpath(".//*[@id='thisForm']/table[8]/tbody/tr[5]/td/input[1]").click()
        time.sleep(2)
        self.switch_window('SonicWall - Upload Firmware')
#        driver.find_element_by_css_selector("input.button").click()
#        driver.find_element_by_name("firmware").clear()
#        driver.find_element_by_name("firmware").send_keys("D:\\vmware-operate\\sw_tz-300_eng_6.5.0.0_6.5.0_5n_987910.sig")
#        driver.find_element_by_name("ok").click()
        upload = driver.find_element_by_name('firmware')
        upload.click()
        '''
        SendKeys.SendKeys('////\\\\10.190.202.40\Firmware\NG\\6.5.0.0-5n\TZ-300\sw_tz-300_eng_6.5.0.0_6.5.0_5n_987910.sig')
        SendKeys.SendKeys('{ENTER}')
        '''
        time.sleep(2)
        # win32
        diaglog = win32gui.FindWindow('#32770', u'文件上传')
        print diaglog
        ComboBoxEx32 = win32gui.FindWindowEx(diaglog, 0, 'ComboBoxEx32', None)
        print ComboBoxEx32
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        print Edit
        button = win32gui.FindWindowEx(diaglog, 0, 'Button', None)
        print button
        time.sleep(1)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, '\\\\10.190.202.40\\Firmware\\NG\\6.2.7.7-2n\\TZ-600\\sw_tz-600_eng_6.2.7.7_6.2.7.7_2n_974136.sig')
        time.sleep(1)
        win32gui.SendMessage(diaglog, win32con.WM_COMMAND, 1, button)
        time.sleep(1)
        '''
        b = win32gui.GetDlgItem(diaglog, 2)
        print  b
        win32gui.SendMessage(diaglog, win32con.WM_COMMAND, 2, b)
        '''
        #driver.switch_to.default_window()
       # win32gui.SendMessage(diaglog, win32con.WM_CLOSE)
        driver.find_element_by_name("ok").click()

        self.switch_to_default_window()

        '''
        handle1 = driver.current_window_handle
        print handle1
        handles = driver.window_handles
        print driver.title
        print handles
        for handle in handles:
            #driver.switch_to.window(handle)
            if handle != handle1:
                driver.switch_to.window(handle)


        time.sleep(20)
        print driver.title
        '''

    def test_boot_new_firmware(self):
        driver = self.driver
        self.switch_to_settings()

        driver.switch_to.default_content()
        driver.switch_to.frame("tabFrame")
#        driver.find_element_by_xpath(".//*[@id='thisForm']/table[8]/tbody/tr[8]/td/input[1]").click()
#        time.sleep(2)
#        self.switch_window('SonicWall - Upload Firmware')
#        driver.find_element_by_css_selector("input.button").click()
#        driver.find_element_by_name("firmware").clear()
#        driver.find_element_by_name("firmware").send_keys("D:\\vmware-operate\\sw_tz-300_eng_6.5.0.0_6.5.0_5n_987910.sig")
#        driver.find_element_by_name("ok").click()
        '''
        driver.find_element_by_xpath(".//*[@id='thisForm']/table[8]/tbody/tr[8]/td/input[1]").click()
        time.sleep(2)

        self.switch_window('SonicWall - Upload Firmware')
        upload = driver.find_element_by_name('firmware')
        upload.click()
#        SendKeys.SendKeys('////\\\\10.190.202.40\\Firmware\\NG\\6.2.7.7-2n\\TZ-600\\sw_tz-600_eng_6.2.7.7_6.2.7.7_2n_974136.sig')
#        SendKeys.SendKeys('{ENTER}')
        diaglog = win32gui.FindWindow('#32770', u'文件上传')
        print diaglog
        ComboBoxEx32 = win32gui.FindWindowEx(diaglog, 0, 'ComboBoxEx32', None)
        print ComboBoxEx32
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        print Edit
        button = win32gui.FindWindowEx(diaglog, 0, 'Button', None)
        print button
        time.sleep(1)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, '\\\\10.190.202.40\\Firmware\\NG\\6.2.7.7-2n\\TZ-600\\sw_tz-600_eng_6.2.7.7_6.2.7.7_2n_974136.sig')
        time.sleep(1)
        win32gui.SendMessage(diaglog, win32con.WM_COMMAND, 1, button)
        driver.find_element_by_name("ok").click()
        time.sleep(20)
        '''
        try:
            button = driver.find_element_by_xpath(".//*[@id='thisForm']/table[8]/tbody/tr[5]/td[6]/a/img")
            driver.execute_script("arguments[0].click();", button)
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
            alert1 = driver.switch_to.alert
            alert1.accept()
        except:
            print 'please upload the new firmware'
            self.switch_to_default_window()
            return False


    def test_export_pref(self):
        driver = self.driver
        self.switch_to_settings()
        driver.switch_to.default_content()
        driver.switch_to.frame("tabFrame")
        driver.find_element_by_xpath(".//*[@id='thisForm']/table[4]/tbody/tr/td[2]/input").click()

        self.switch_window('Export Settings')
        driver.find_element_by_name("ok").click()
        time.sleep(6)
        print 'teeees'
        '''
        SendKeys.SendKeys('{TAB}')
        print 'dddd'
        SendKeys.SendKeys('{TAB}')
        SendKeys.SendKeys('{TAB}')
        print 'dsdfasdf'
        '''
        SendKeys.SendKeys('{ENTER}')
        print 'ddddd'



        '''
        SendKeys.SendKeys('{ENTER}')
        print 'ggg'
        time.sleep(2)
        SendKeys.SendKeys('{ENTER}')
        print 'tesdss'
        dialog = win32gui.FindWindow('MozillaDialogClass', u'正在打开 sonicwall-TZ_600-6_2_7_1-23n.exp')
        print dialog
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        print button
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        '''

    def test_enable_firewall_settings(self):
        driver = self.driver
        print driver.get_cookies()
        self.switch_to_firewall_Settings()
        driver.switch_to.default_content()
        driver.switch_to.frame("tabFrame")
        try:
            inputs = driver.find_elements_by_tag_name('input')
            for input in inputs:
                if input.get_attribute('type') == 'checkbox':
                    input.click()
                    time.sleep(1)
        except:
            driver.get_screenshot_as_png("D:\\vmware-operate\\screenshot\\firewall_setting.png")
        '''
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        test = soup.find_all('label')

        lst1 = []
        for i in range(0, len(test)):
        #    print str(test[i])
            lst1.append(str(test[i]))
        print lst1
        print len(lst1)
      #  for i in range(0, len(lst1)):
            print lst1[i]

        test1 = soup.find_all('input')
        lst2=[]
        for i in range(0, len(test1)):
            if 'checkbox' in str(test1[i]) or 'radio' in str(test1[i]):
                lst2.append(str(test1[i]))
        print lst2
        print len(lst2)
        dict1 = dict(zip(lst2, lst1))
        print dict1
  #      for key, value in dict1.iteritems():
   #         print key, value
        '''
        print driver.find_element_by_id('enableStealthMode0').is_selected()
        if driver.find_element_by_id('enableStealthMode0').is_selected():
            pass
        else:
            driver.find_element_by_id('enableStealthMode0').click()
        driver.find_element_by_id('DecrementHopLimit0').click()
        driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
        time.sleep(2)


        time.sleep(2)
        button = driver.find_element_by_name('applyButt')
        driver.execute_script("arguments[0].click()", button)
        self.switch_to_default_window()






test = login()
test.login_web()
#test.test_enable_firewall_settings()
#test.test_add_ao()
#test.test_upload_firmware()
#test.switch_to_default_window()
test.add_vpn_policy()
#test.test_upload_firmware()
test.test_enable_firewall_settings()
if test.test_boot_new_firmware() == False:
    test.test_upload_firmware()
    test.test_boot_new_firmware()
else:
    test.test_boot_new_firmware()
#test.test_enable_firewall_settings()
#test.logout()