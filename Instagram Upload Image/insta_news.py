
# import sys
# sys.setrecursionlimit(50000)

from instagrapi import Client
import requests, random, os
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

try: os.mkdir('images')
except: pass

news_api = input('\nEnter NewsAPI Key : ')
passwd = input('\nEnter Instagram Password : ')

source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
source = random.choice(source)

gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={news_api}'

req = requests.get(gets)
box = req.json()['articles']
cap = []

def make_square(im, j, min_size=256, fill_color=(255,255,255,0)):
    img = Image.open(im)
    x, y = img.size

    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)

    new_im = new_im.convert("RGB")
    new_im.paste(img, (int((size - x) / 2), int((size - y) / 2)))

    I1 = ImageDraw.Draw(new_im)
    myFont = ImageFont.truetype("arial.ttf", 30)

    I1.text((15, 15), f'[ {j+1} ]', font=myFont, fill=(0, 0, 0))
    new_im.save(im)

for j, i in enumerate(box):
    tweet = f'({j+1}). {i["title"]}\n'
    cap.append(tweet)
    img = i['urlToImage']
    r = requests.get(img, allow_redirects=True)

    path = f'images/{j}.jpg'
    open(path, 'wb').write(r.content)
    make_square(path, j)

bot = Client()
user = 'vix.bot'

bot.login(username = user, password = passwd)
album_path = ['images/'+i for i in os.listdir('images')]

text = f'Read More:\n https://googleadsense.pythonanywhere.com/news/{source}\n\n'
bot.album_upload(
    album_path,
    caption = text + '\n'.join(cap)
)
