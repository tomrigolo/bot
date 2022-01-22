import time 
import subprocess


def scan(lien,chapter_start,nbr_chapters):
    for i in range(nbr_chapters):
        chapter_start += i
        lien_dl = (f"{lien}{chapter_start}")
        print(lien_dl)
        subprocess.Popen(f"E:/Python3/Python/bot/Selenium/Scan/dl.py {lien_dl}")



if __name__ == "__main__":
    scan("https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-", 2 ,1)