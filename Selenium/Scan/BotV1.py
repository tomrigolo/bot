import requests



def scan(lien,chapter_start,nbr_chapters):
    for i in range(nbr_chapters):
        chapter_start += i
        lien_dl = (f"{lien}{chapter_start}")
        dl(lien_dl)
        
        
def dl(lien):
    request = requests.get(lien)
    with open(f'E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru .html','ab') as f:
        f.write(request.content)
    
    
if __name__ == "__main__":    
    scan("https://ww1.mangakakalot.tv/chapter/manga-bs978875/chapter-", 2 ,4)