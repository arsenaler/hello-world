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


def get_id(soup):
#    with open('router.html.txt', 'r') as f:
#        soup = BeautifulSoup(f, 'lxml')
    lst5 = []
    lst4 = soup.select('input[name="object_ids"]')
    lst6 = str(lst4).split(',')

    for k in range(0, len(lst6)):
        h = lst6[k].strip(' ').split(' ')[4].split('\"')[1]
        lst5.append(h)
    return lst5

#print soup.find_all('input',class_='table-row-multi-select')
#print soup.find_all(class_='table-row-multi-select')
#print soup.select('input[name="object_ids"]')
#print soup.select('a[href=re.compile("/dashboard/admin/routers/")]')
def get_name(soup):
    lst2 = []
    lst = soup.find_all(href=re.compile('/dashboard/admin/routers/'))
    for i in range(0, len(lst)):
        string1 = str(lst[i])
        if 'test' in string1:
            lst1 = list(set(string1.split(" ")))
            for j  in range(0,len(lst1)):
                if 'test' in lst1[j]:
                    lst2.append(lst1[j].strip('/\n'))
    return lst2
class login(object):
#   def __init__(self):
#       self.base_url = "http://10.8.42.2/"
    @classmethod
    def login_web(cls):
        cls.base_url = "http://10.8.42.2/"
        driver = cls.driver = webdriver.Firefox()
        driver.implicitly_wait(30)
#        base_url = "http://10.8.42.2/"

        driver.get(cls.base_url + "/dashboard/auth/login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_xpath("//button[@type='submit']").click()
#driver.get(base_url + "/dashboard/admin/routers")
    @classmethod
    def add_router(cls, m, n):
        login()
        driver = cls.driver
        driver.get(cls.base_url + "/dashboard/project/routers/")
        html = driver.page_source
        soup1 = BeautifulSoup(html, 'lxml')
        router1 = get_id(soup1)
#driver.find_element_by_css_selector("dt > div").click()
#driver.find_element_by_link_text(u"路由").click()
        for i in range(m, n):
            driver.find_element_by_id("Routers__action_create").click()
            driver.find_element_by_id("id_name").clear()
            driver.find_element_by_id("id_name").send_keys("test"+str(i))
            driver.find_element_by_xpath(u"//input[@value='新建路由']").click()
            time.sleep(5)

        driver.get(cls.base_url + "/dashboard/project/routers/")
        html1 = driver.page_source
        soup2 = BeautifulSoup(html1, 'lxml')
        router4 = get_id(soup2)
        router5 = [i for i in router4 if i not in router1]
        print router5
        for index, value in enumerate(router5):
            print "Routers__row_" + value + "__action_setgateway"
            driver.find_element_by_id("Routers__row_" + value + "__action_setgateway").click()
            Select(driver.find_element_by_id("id_network_id")).select_by_visible_text("net04_ext")
#    driver.find_element_by_css_selector("option[value=\"f4f56079-84e1-41ac-bc5d-ebeef5699220\"]").click()
            driver.find_element_by_xpath(u"//input[@value='设置网关']").click()
            time.sleep(5)
    @classmethod
    def add_network(cls, m, n):
        driver = cls.driver
        driver.get(cls.base_url+"/dashboard/project/networks/")
        lock = threading.Lock()
        for i in range(m, n):
            if lock.acquire():
                driver.find_element_by_id("networks__action_create").click()
                driver.find_element_by_id("id_net_name").clear()
                driver.find_element_by_id("id_net_name").send_keys("network" + str(i))
                driver.find_element_by_link_text(u"子网").click()
                driver.find_element_by_id("id_subnet_name").clear()
                driver.find_element_by_id("id_subnet_name").send_keys("network"+str(i))
                driver.find_element_by_id("id_cidr").clear()
                driver.find_element_by_id("id_cidr").send_keys("10." + str(i) + ".1.0/24")
                driver.find_element_by_id("id_gateway_ip").clear()
                driver.find_element_by_id("id_gateway_ip").send_keys("10." + str(i) + ".1.1")
        #    driver.find_element_by_link_text(u"子网详情").click()
                driver.find_element_by_xpath(".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[1]").click()
                driver.find_element_by_xpath(".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[2]").click()
                time.sleep(3)
                lock.release()
    @classmethod
    def del_network(cls):
        driver = cls.driver
        driver.get(cls.base_url + "/dashboard/project/networks/")
        html1 = cls.driver.page_source
        soup2 = BeautifulSoup(html1, 'lxml')

  #      network1 = []
        network1 = get_id(soup2)
        for index, value in enumerate(network1):
            driver.find_element_by_css_selector("#networks__row__" + value + "> td.multi_select_column > input[name=\"object_ids\"]").click()
            driver.find_element_by_id("networks__action_delete").click()
            driver.find_element_by_link_text(u"删除网络").click()
            time.sleep(3)

    @classmethod
    def switch_to_windows(cls, window_name):
        login.login_web()
        driver = cls.driver
        print driver.title
        driver.switch_to_default_content()
        nowhandler = driver.current_window_handle
        handles = driver.window_handles
        driver.get(cls.base_url + "/dashboard/project/networks/")
        driver.find_element_by_id("networks__action_create").click()
        print handles
        for handle in handles:
            driver.switch_to_window(handle)
            print driver.title
            if driver.title == window_name:
                driver.switch_to_window(handle)
                break
        time.sleep(10)



    @classmethod
    def logout(cls):
        cls.driver.quit()

#login.login_web()
#a.add_network(1,6)
#a.del_network()
'''
a1 = time.time()
threads = []
t1 = threading.Thread(login.add_network(1, 6))
threads.append(t1)
t2 = threading.Thread(login.del_network())
threads.append(t2)
lock = threading.RLock()
for t in threads:
    if lock.acquire():
        t.start

for t in threads:
    t.join
b = time.time()
print b-a1
'''
login.switch_to_windows("网络 - OpenStack Dashboard")


login.logout()