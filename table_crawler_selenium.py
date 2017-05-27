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

#crawler.gettable(yy, mm, c_list[c_num])

def gettable(current_year, current_month, classname):

    with open('/py3_file/template_0.html') as f_1:
        with open('/var/www/html/tables/' + classname + '.html', 'w', encoding = 'utf-8') as f_2:
            f_2.write(f_1.read())
            f_2.write(classname)
            f_2.write('</title>')
            f_2.write('</head>')
            f_2.write('<body>')

    url = "http://140.115.236.11/first.asp"
    
    driver = webdriver.PhantomJS('/py3_file/phantomjs') # or add to your PATH
    driver.set_window_size(1024, 768) # optional
    #driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver/chromedriver.exe')
    driver.get(url)
    
    for m in range(current_month-7, current_month):
        y = current_year
        if m < 1:
            y = current_year - 1
        if m % 12 == 0:
            m = 12
        else:
            m = m % 12
        
        driver.switch_to_window(driver.window_handles[0])
        Select(driver.find_element_by_name('YY')).select_by_value(str(y))
        Select(driver.find_element_by_name('MM')).select_by_value(str(m))
        driver.find_element_by_name('NEXT').click()
        driver.implicitly_wait(3)

        driver.switch_to_window(driver.window_handles[1])
        try:
            Select(driver.find_element_by_name('STR')).select_by_value(classname)
            driver.find_element_by_name('Query').click()
            driver.implicitly_wait(3)

            driver.switch_to_window(driver.window_handles[2])
            soup_table = BeautifulSoup(driver.page_source, 'lxml')

            with open('/var/www/html/tables/' + classname + '.html', 'a', encoding = 'utf-8') as f:
                f.write(str(soup_table.select('form')[0]))
        except:
            continue
        
    
    with open('/var/www/html/tables/' + classname + '.html', 'a', encoding = 'utf-8') as f_2:
        f_2.write('<div id="skipId"></div>')
    
    y = current_year

    for m in range(current_month, current_month + 7):
        
        if m > 12:
            y = current_year + 1
            m = m % 12
        
        driver.switch_to_window(driver.window_handles[0])
        Select(driver.find_element_by_name('YY')).select_by_value(str(y))
        Select(driver.find_element_by_name('MM')).select_by_value(str(m))
        driver.find_element_by_name('NEXT').click()
        driver.implicitly_wait(3)

        driver.switch_to_window(driver.window_handles[1])
        try:
            Select(driver.find_element_by_name('STR')).select_by_value(classname)
            driver.find_element_by_name('Query').click()
            driver.implicitly_wait(3)

            driver.switch_to_window(driver.window_handles[2])
            soup_table = BeautifulSoup(driver.page_source, 'lxml')

            with open('/var/www/html/tables/' + classname + '.html', 'a', encoding = 'utf-8') as f:
                f.write(str(soup_table.select('form')[0]))
        except:
            break
        
    with open('/var/www/html/tables/' + classname + '.html', 'a', encoding = 'utf-8') as f:
        f.write('</body>')
        f.write('</html>')
    driver.quit()