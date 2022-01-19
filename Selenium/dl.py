import requests
import sys

def dl(lien,episode):
    request = requests.get(lien)
    with open(f'E:\Anime\One Piece\One Piece Episode {episode}.mp4','wb') as f:
        f.write(request.content)

episode = int(sys.argv[1])
lien_dl = str(sys.argv[2])



    
dl(lien_dl,episode)