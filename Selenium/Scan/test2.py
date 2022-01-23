from selenium import webdriver
import time

PATH = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
CHEMIN_DOSSIER = "E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-"
FORMAT = "html"
SCROLL_PAUSE_TIME = 0.1

if __name__ == "__main__":
    driver = webdriver.Chrome(PATH)
    driver.get(f'{LIEN_MANGA}1')
    i = 0
    height = driver.execute_script("return document.body.scrollHeight")
    while i < height:
        driver.execute_script(f"window.scrollTo(0, {i*1080})")
        time.sleep(SCROLL_PAUSE_TIME)
        height = driver.execute_script("return document.body.scrollHeight")
        i += 1
        