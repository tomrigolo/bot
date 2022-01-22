import requests
import sys

def dl(lien):
    request = requests.get(lien)
    with open(f'E:\Scan\Sono Bisque Doll Wa Koi Wo Suru\Sono Bisque Doll Wa Koi Wo Suru .html','ab') as f:
        f.write(request.content)


dl(str(sys.argv[1]))