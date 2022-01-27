from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
#from pywebcopy.core import save_webpage

print(f"{os.getcwd()}\\chromedriver.exe")
"""PATH = f"{os.getcwd}\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(f'https://ww1.mangakakalot.tv/chapter/manga-zy953881/chapter-1')
time.sleep(2)
"""

driver = webdriver.Chrome(f"{os.getcwd()}\\chromedriver.exe")
driver.get(f'https://ww1.mangakakalot.tv/chapter/manga-zy953881/chapter-1')

#save_webpage(url = 'https://ww1.mangakakalot.tv/chapter/manga-zy953881/chapter-1', mirrors_dir = 'E:/Scan/test')

#driver.quit()