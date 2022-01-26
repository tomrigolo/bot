import requests
from selenium import webdriver
import time
import pyautogui
import os
import pyperclip


PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
NOM_FICHIER = "/Sono Bisque Doll Wa Koi Wo Suru"
CHEMIN_DOSSIER = "E:/Scan/Sono Bisque Doll Wa Koi Wo Suru"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-"
FORMAT = ".html"


CHAPTEUR_START = 40
NBR_CHAPTEURS = 69-35

PAUSE_KEY = 0.5
SCROLL_PAUSE_TIME = 0.2
PAUSE_DL = 15
PAUSE_CHARGEMENT_PAGE = 0.5
MONITOR_HEIGHT = 1080

def _workaround_write(text):
    """
    This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
    It copies the text to clipboard and pastes it, instead of typing it.
    """
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')

def scan(lien,chemin_dossier,nom_fichier,format_fichier,chapter_start,nbr_chapters):
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
        
def dl(lien,chemin,fichier,chapteur,format):
    pyautogui.hotkey('ctrl', 's')
    time.sleep(PAUSE_KEY)
    pyautogui.write(f'Nisekoi chapteurs {chapteur}')
    time.sleep(PAUSE_KEY)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(PAUSE_KEY)
    _workaround_write(f'{chemin}')
    time.sleep(PAUSE_KEY)
    pyautogui.press('enter')
    time.sleep(PAUSE_KEY)
    for i in range(9):
        pyautogui.press('tab')
        time.sleep(PAUSE_KEY)
    pyautogui.press('enter')
    
    
    
if __name__ == "__main__":
    driver = webdriver.Chrome(PATH_CHROME)
    scan(LIEN_MANGA, CHEMIN_DOSSIER,NOM_FICHIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    driver.close()
    