import requests
from selenium import webdriver
import time
import pyautogui
import os



PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
NOM_FICHIER = "/Nisekoi"
CHEMIN_DOSSIER = "E:/Scan/Nisekoi"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-kw951979/chapter-"
FORMAT = ".html"

CHAPTEUR_START = 1
NBR_CHAPTEURS = 1

SCROLL_PAUSE_TIME = 0.2
PAUSE_DL = 10
PAUSE_CHARGEMENT_PAGE = 0.5
MONITOR_HEIGHT = 1080

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
    #driver.close()
        
def dl(lien,chemin,fichier,chapteur,format):
    pyautogui.hotkey('ctrl', 's')
    time.sleep(0.5)
    pyautogui.write(f'Nisekoi')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.write(f'E:\\Scan\\Nisekoi')
    """time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('enter')"""
    
    
    
if __name__ == "__main__":
    driver = webdriver.Chrome(PATH_CHROME)
    scan(LIEN_MANGA, CHEMIN_DOSSIER,NOM_FICHIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    