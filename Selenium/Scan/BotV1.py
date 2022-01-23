import requests
from selenium import webdriver
import time


PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
CHEMIN_DOSSIER = "E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-"
FORMAT = "html"
SCROLL_PAUSE_TIME = 0.1
NBR_CHAPTEURS = 10
CHAPTEUR_START = 1
PAUSE_DL = 1

def scan(lien,chemin_dossier,format_fichier,chapter_start,nbr_chapters):
    driver = webdriver.Chrome(PATH_CHROME)
    for j in range(nbr_chapters):
        chapter_start += j
        lien_dl = (f'{lien}{chapter_start}')
        driver.get(f'{lien_dl}')
        for i in range(80):
            y = i*1080
            driver.execute_script(f"window.scrollTo(0, {y})")
            time.sleep(SCROLL_PAUSE_TIME)
        dl(lien_dl,chemin_dossier,format_fichier)
        time.sleep(PAUSE_DL)
    driver.close()
        
def dl(lien,chemin,format):
    request = requests.get(lien)
    with open(f'{chemin} .{format}','ab') as f:
        f.write(request.content)
    
if __name__ == "__main__":
    scan(LIEN_MANGA, CHEMIN_DOSSIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    