import requests
import sys

def dl(lien,chapter):
    request = requests.get(lien+chapter)
    with open(f'E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru .html','wb') as f:
        f.write(request.content)


dl(str(sys.argv[1]), str(sys.argv[2]))