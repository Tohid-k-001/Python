import requests
url="http://pngimg.com/uploads/anime_girl/anime_girl_PNG88.png"
r=requests.get(url)
print(r.content)