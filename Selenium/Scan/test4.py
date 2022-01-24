import pyautogui
import os
import time


os.system("start opera")
time.sleep(2)
pyautogui.hotkey('ctrl', 'e')
pyautogui.write('ww1.mangakakalot.tv/chapter/manga-zy953881/chapter-2')
time.sleep(1)
#pyautogui.press('down')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('pagedown')
#pyautogui.hotkey('windows', 'r')