
# https://platform.openai.com/account/api-keys

import getpass, openai, shutil
import requests, time, os, random
from instabot import Bot
from PIL import Image

try:
    shutil.rmtree('config')
except:
    pass

try:
    os.mkdir('to_upload')
except:
    pass

try:
    os.mkdir('images')
except:
    pass

user = ['vix.bot', '_____.___alone___._____', 'imvickykumar999']
passwd = getpass.getpass('Enter Instagram Password : ')

API_Key = getpass.getpass('Enter API key : ')
openai.api_key = API_Key

models = openai.Model.list()
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                messages=[{"role": "user", 
                           "content": "Trending Video Games"}])

topics = completion.choices[0].message.content
topic = random.choice(topics.split('\n')[2:-2]).split('. ')[1]

n=1
image_resp = openai.Image.create(prompt=topic, n=n, size="512x512")
file = time.time()

for i in range(n):
    img = list(image_resp['data'][i].values())[0]
    r = requests.get(img, allow_redirects=True)
    open(f'images/{file}.jpg', 'wb').write(r.content)

bot = Bot()
bot.login(username = user[0], password = passwd)

def make_square(im, min_size=256, fill_color=(255,255,255,0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)

    new_im = new_im.convert("RGB")
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

path = f'images/{file}.jpg'
test_image = Image.open(path)
new_image = make_square(test_image)

path = f'to_upload/{file}.jpg'
new_image.save(path)

cap = f'🔥 This is Trending Video-Game image of "{topic}", created by OpenAI API and uploaded at {file} (unix time) using InstaBot package written in Python Language 💡' 
bot.upload_photo(path, caption = cap)
