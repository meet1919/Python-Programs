from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

browser = webdriver.Chrome()
browser.get('http://imgur.com/')

search = browser.find_element_by_class_name('Searchbar-textInput')
search.send_keys('Cats')
search.send_keys(Keys.ENTER)

browser.find_element_by_xpath('//*[@id="bmFaD"]/a').click()
gif = browser.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/img[2]').get_attribute('src')

res = requests.get(gif)
with open('cat.gif', 'wb') as file:
    file.write(res.content)