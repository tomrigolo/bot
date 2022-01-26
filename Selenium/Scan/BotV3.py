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
NBR_CHAPTEURS = 1

SCROLL_PAUSE_TIME = 0.1
PAUSE_DL = 0.09
PAUSE_CHARGEMENT_PAGE = 1
PAUSE_KEY = 0.5
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
    os.system("start opera")
    time.sleep(PAUSE_CHARGEMENT_PAGE)
    for j in range(nbr_chapters):
        chapteur = chapter_start + j
        pyautogui.hotkey('ctrl', 'e')
        _workaround_write(f"{lien}{chapteur}")
        time.sleep(PAUSE_KEY)
        pyautogui.press('enter')
        time.sleep(PAUSE_CHARGEMENT_PAGE)
        for k in range(100):
            pyautogui.press("pagedown")
            time.sleep(SCROLL_PAUSE_TIME)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(PAUSE_CHARGEMENT_PAGE)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(PAUSE_KEY)
        _workaround_write(f"{chemin_dossier}")
        time.sleep(PAUSE_KEY)
        pyautogui.press('enter')
        time.sleep(PAUSE_KEY)
        pyautogui.hotkey('ctrl', 'shift','n')
        time.sleep(PAUSE_KEY)
        _workaround_write(f"Chapteur {chapteur}")
        pyautogui.press('enter')
        time.sleep(PAUSE_KEY)
        pyautogui.press('enter')
        time.sleep(PAUSE_KEY)
        for i in range(5):
            pyautogui.press('tab')
            time.sleep(PAUSE_KEY)
        pyautogui.press('enter')
        
    
if __name__ == "__main__":
    scan(LIEN_MANGA, CHEMIN_DOSSIER,NOM_FICHIER, FORMAT, CHAPTEUR_START, NBR_CHAPTEURS)
    