from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

print('----Welcome to PyMail----')
print()
print('Hey O.G. Welcome Back')
print('↓ Provide me some details below ↓')
print()

input('Enter recipient Email Address: ')
input('Type what you want to send: ')

browser = webdriver.Chrome()
browser.get('http://mail.google.com/')

email = browser.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys(os.getenv('EMAIL_USER'))
browser.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

print(browser.current_url)

password = browser.find_element_by_xpath('//*[@id="identifierId"]')
password.send_keys(os.getenv('EMAIL_PASS'))
browser.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

