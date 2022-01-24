import pyautogui
import os
import time
import pyperclip

def _workaround_write(text):
    """
    This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
    It copies the text to clipboard and pastes it, instead of typing it.
    """
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')


pyautogui.hotkey('win', 'e')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'l')
time.sleep(0.5)
_workaround_write("E:/Scan/test")
time.sleep(0.5)
pyautogui.press('enter')