from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://gabrielecirulli.github.io/2048/')
game = browser.find_element_by_tag_name('html')
for i in range(200):
    game.send_keys(Keys.ARROW_RIGHT)
    game.send_keys(Keys.ARROW_DOWN)
    game.send_keys(Keys.ARROW_LEFT)
    game.send_keys(Keys.ARROW_UP)


