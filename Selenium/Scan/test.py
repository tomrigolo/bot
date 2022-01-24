from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from pywebcopy.core import save_webpage


PATH = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(f'https://ww1.mangakakalot.tv/chapter/manga-zy953881/chapter-1')
time.sleep(2)

save_me = ActionChains(driver).key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s')
save_me.perform()

#driver.quit()