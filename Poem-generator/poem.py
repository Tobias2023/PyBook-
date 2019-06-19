# make sure to have the webdriver file in directory
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\\chromedriver.exe"

# New chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Goto poem website
open_webpage = 'https://www.poetryfoundation.org/poems/poem-of-the-day'
driver.get(open_webpage)
sleep(3)

poem = driver.find_elements_by_class_name("o-poem")

print(poem[0].text)

driver.quit()
