import requests
from selenium import webdriver
import time



PATH_CHROME = "C:/Users/utilisateur/Desktop/Python/bot/Selenium/Scan/chromedriver.exe"
NOM_FICHIER = "/Sono Bisque Doll Wa Koi Wo Suru"
CHEMIN_DOSSIER = "C:/Users/utilisateur/Desktop/Scan/Sono Bisque Doll Wa Koi Wo Suru"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-"
FORMAT = ".html"

CHAPTEUR_START = 68
NBR_CHAPTEURS = 2

SCROLL_PAUSE_TIME = 0.1
PAUSE_DL = 0.09
PAUSE_CHARGEMENT_PAGE = 0.5
MONITOR_HEIGHT = 1080

def scan(lien,chemin_dossier,nom_fichier,format_fichier,chapter_start,nbr_chapters):
    driver = webdriver.Chrome(PATH_CHROME)
    for j in range(nbr_chapters):
        chapter_to_dl = chapter_start + j
        lien_dl = (f'{lien}{chapter_to_dl}')
        driver.get(f'{lien_dl}')
        time.sleep(PAUSE_CHARGEMENT_PAGE)
        i = 0
        height = driver.execute_script("return document.body.scrollHeight")
        while i < height/MONITOR_HEIGHT:
            y = i*MONITOR_HEIGHT
            driver.execute_script(f"window.scrollTo(0, {y})")
            time.sleep(SCROLL_PAUSE_TIME)
            height = driver.execute_script("return document.body.scrollHeight")
            i+=1
        dl(lien_dl,chemin_dossier,nom_fichier,chapter_to_dl,format_fichier)
        time.sleep(PAUSE_DL)
    driver.close()
        
def dl(lien,chemin,fichier,chapteur,format):
    request = requests.get(lien)
    with open(f'{chemin}{fichier} chapteur {chapteur}{format}','wb') as f:
        f.write(request.content)
    
if __name__ == "__main__":
    scan(LIEN_MANGA, CHEMIN_DOSSIER,NOM_FICHIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    