from genericpath import isdir
from importlib.resources import path
import requests
import time
from bs4 import BeautifulSoup
import os


PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
NOM_FICHIER = "Fairy Tail"
CHEMIN_DOSSIER = "E:/Scan/Fairy Tail"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-tk952067/chapter-"
FORMAT = ".html"

CHAPTEUR_START = 1
NBR_CHAPTEURS = 1

SCROLL_PAUSE_TIME = 0.085
PAUSE_DL = 0.09
PAUSE_CHARGEMENT_PAGE = 0.5
MONITOR_HEIGHT = 1080

def scan(lien,chemin_dossier,format_fichier,chapter_start,nbr_chapters):
    for j in range(nbr_chapters):
        chapter_to_dl = chapter_start + j
        lien_dl = (f'{lien}{chapter_to_dl}')
        dl(lien_dl,chemin_dossier,chapter_to_dl,format_fichier)
        time.sleep(PAUSE_DL)
        
def dl(lien,chemin,chapteur,format):
    if not os.path.isdir(f"{CHEMIN_DOSSIER}/asset"):
        os.mkdir(f"{CHEMIN_DOSSIER}/asset")
    request = requests.get(lien)
    soup = BeautifulSoup(request.content, 'html.parser')
    for index,img in enumerate( soup.find_all('img')):
        if "data-src" in img:
            img["src"] = img["data-src"]
            del img["data-src"]
        if "src" not in img or img["src"][0] != "h":
            continue
        extension = img["src"].split(".")[1]
        img_name = f'{chapteur}-{index}'
        with open (f'{chemin}/asset/{img_name}.{extension}','wb') as fimg:
            fimg.write(requests.get(img["src"]).content)
        img["src"] = f'./asset/{img_name}.{extension}'
            
    with open(f'{chemin}/{NOM_FICHIER} chapteur {chapteur}{format}','wb') as f:
        f.write(str(soup).encode("utf-8"))

    
    
    
if __name__ == "__main__":
    scan(LIEN_MANGA, CHEMIN_DOSSIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    