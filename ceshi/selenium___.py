# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome('F:\python新环境搭建\chromedriver_win32\chorme\Chrome-48.0.2564.97\\chromedriver.exe')
driver.get('http://www.ccgp-weifang.gov.cn')
source = driver.page_source
print(1)
