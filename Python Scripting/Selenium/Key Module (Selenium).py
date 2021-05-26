from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('http://nostarch.com')
try:
    htmlelem = browser.find_element_by_tag_name('html')
    htmlelem.send_keys(Keys.END)
    time.sleep(3)
    htmlelem.send_keys(Keys.HOME)
    time.sleep(2)
    browser.quit()
except:
    print('Couldn\'t find element')
