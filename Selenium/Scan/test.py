import requests
import sys

def dl(lien,chapteur):
    request = requests.get(lien)
    with open(f'E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru .html','wb') as f:
        f.write(request.content)


dl("https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-2")