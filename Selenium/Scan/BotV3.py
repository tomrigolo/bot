import time
import pyautogui
import os
import pyperclip


PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
NOM_FICHIER = "/Nisekoi"
CHEMIN_DOSSIER = "E:/Scan/Nisekoi"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-kw951979/chapter-"
FORMAT = ".html"

CHAPTEUR_START = 1
NBR_CHAPTEURS = 2

SCROLL_PAUSE_TIME = 0.1
PAUSE_DL = 0.09
PAUSE_CHARGEMENT_PAGE = 1
MONITOR_HEIGHT = 1080

def scan(lien,chemin_dossier,nom_fichier,format_fichier,chapter_start,nbr_chapters):
    os.system("start chrome")
    time.sleep(PAUSE_CHARGEMENT_PAGE)
    for j in range(nbr_chapters):
        pyautogui.hotkey('ctrl', 'e')
        
        
    
if __name__ == "__main__":
    scan(LIEN_MANGA, CHEMIN_DOSSIER,NOM_FICHIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    