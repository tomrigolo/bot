import requests
from selenium import webdriver
import time


PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
CHEMIN_DOSSIER = "E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-"
FORMAT = "html"
SCROLL_PAUSE_TIME = 0.5


if __name__ == "__main__":    
    driver = webdriver.Chrome(PATH_CHROME)
    driver.get(f'{LIEN_MANGA}1')
    last_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(SCROLL_PAUSE_TIME)
    driver.close()