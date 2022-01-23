import requests
from selenium import webdriver


PATH_CHROME = "E:/Python3/Python/bot/Selenium/Scan/chromedriver.exe"
CHEMIN_DOSSIER = "E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru"
LIEN_MANGA = "https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-"
FORMAT = "html"


def scan(lien,chemin_dossier,format,chapter_start,nbr_chapters):
    for i in range(nbr_chapters):
        chapter_start += i
        lien_dl = (f"{lien}{chapter_start}")
        dl(lien_dl,chemin_dossier,format)
        
def dl(lien,chemin,format):
    request = requests.get(lien)
    with open(f'{chemin} .{format}','ab') as f:
        f.write(request.content)
    
if __name__ == "__main__":    
    driver = webdriver.Chrome(PATH_CHROME)
    scan(LIEN_MANGA,CHEMIN_DOSSIER,FORMAT, 2 ,4)
    driver.close()