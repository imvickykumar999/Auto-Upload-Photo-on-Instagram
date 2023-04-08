
# https://github.com/imvickykumar999/Download-Reels

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
# passwd = '************'

# https://platform.openai.com/account/api-keys
API_Key = getpass.getpass('Enter API key : ')

# API_Key = '***********************************'
openai.api_key = API_Key

# list models
models = openai.Model.list()

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                messages=[{"role": "user", 
                           "content": "Trending Video Games"}])

topics = completion.choices[0].message.content
topic = random.choice(topics.split('\n')[2:-2]).split('. ')[1]
# topic = input('Enter topic of photo : ')

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

# file = input('Enter Image Name : ')
path = f'images/{file}.jpg'

test_image = Image.open(path)
new_image = make_square(test_image)

path = f'to_upload/{file}.jpg'
new_image.save(path)

cap = f'🔥 This is image of "{topic}" and is created by OpenAI API and uploaded using InstaBot package written in python language 💡' 
bot.upload_photo(path, caption = cap)

try:
    bot.send_message("Image Uploaded", user[1:])
except:
    print('DM NOT sent.')

try:
    shutil.rmtree('config')
except:
    pass
