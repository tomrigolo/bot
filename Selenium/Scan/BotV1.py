import requests
from selenium import webdriver
import time


PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
CHEMIN_DOSSIER = "E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-"
FORMAT = "html"
SCROLL_PAUSE_TIME = 0.05
NBR_CHAPTEURS = 1
CHAPTEUR_START = 1


def scan(lien,chemin_dossier,format,chapter_start,nbr_chapters):
    driver = webdriver.Chrome(PATH_CHROME)
    for j in range(nbr_chapters):
        chapter_start += j
        lien_dl = (f'{lien}{chapter_start}')
        driver.get(f'{lien_dl}')
        i = 0
        height = driver.execute_script("return document.body.scrollHeight")
        while i < 80:
            driver.execute_script(f"window.scrollTo(0, {i*1080})")
            time.sleep(SCROLL_PAUSE_TIME)
            height = driver.execute_script("return document.body.scrollHeight")
            i += 1
        dl(lien_dl,chemin_dossier,format)
    driver.close()
        
def dl(lien,chemin,format):
    request = requests.get(lien)
    with open(f'{chemin} .{format}','ab') as f:
        f.write(request.content)
    
if __name__ == "__main__":
    scan(LIEN_MANGA, CHEMIN_DOSSIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    