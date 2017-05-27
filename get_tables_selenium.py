import string
import random
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

import table_crawler_selenium as crawler
import kill_old_tables
import get_index

tablespath = "/var/www/html/tables/"

url = "http://140.115.236.11/first.asp"

driver = webdriver.PhantomJS('/py3_file/phantomjs')
driver.set_window_size(1024, 768)
driver.get(url)

soup_first = BeautifulSoup(driver.page_source, 'lxml')

for i in range(0,len(soup_first.select('option'))):
    if 'selected' in str(soup_first.select('option')[i]):
        try:
            j = int(soup_first.select('option')[i].text.strip())
            if j >= 1 and j <= 12:
                mm = j
            else:
                yy = j
        except:
            print()

driver.find_element_by_name('NEXT').click()
driver.implicitly_wait(3)

driver.switch_to_window(driver.window_handles[1])


c_list = []

soup_next2 = BeautifulSoup(driver.page_source, 'lxml')

for i in range(0, len(soup_next2.select('option'))):
    c_list.append(soup_next2.select('option')[i].text.strip())

driver.quit()

kill_old_tables.kill_old_tables(c_list, tablespath)

for c_num in range(0, len(c_list)):
    crawler.gettable(yy, mm, c_list[c_num])

get_index.get_index(tablespath)