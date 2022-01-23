import requests
from selenium import webdriver
import time



driver = webdriver.Chrome("E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe")
driver.get(f'https://ww1.mangakakalot.tv/chapter/manga-zy953881/chapter-1')
driver.execute_script("window.scrollTo(0, 1080)")
