from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/curio__city__/')
time.sleep(2)

browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys('curio__city__')
time.sleep(2)

browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys('curiocity12345')
time.sleep(2)

browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
time.sleep(2)

elem = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys('ahmedabadmirrorofficial')




#for i in range(2000):
    #browser.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[3]/div/div[3]/button')[i].click()