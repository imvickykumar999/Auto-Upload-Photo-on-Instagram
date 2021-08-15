import shutil, os
from PIL import Image

try:
    shutil.rmtree('config')
except Exception as e:
    print(e)

if not os.path.exists('toupload'):
  os.mkdir('toupload')
  print('\nThere is no photo in toupload folder !!!')

from instabot import Bot
bot = Bot()

print('Photo should be SQUARE !!!')
link = 'https://github.com/imvickykumar999/Auto-Upload-Photo-on-Instagram'

user = input('Enter Username : ')
passwd = input('Enter Password : ')
bot.login(username = user, password = passwd)

for file in os.listdir('toupload'):
    try:
        img = Image.open('toupload/' + file)
        rgb_img = img.convert('RGB')
        filejpeg =  'toupload/' + file + '.jpeg'
        rgb_img.save(filejpeg)

        bot.upload_photo(filejpeg,
        caption = filejpeg + f' has been upload using {link}')
        # os.rename('toupload/' + filejpeg +'.REMOVE_ME', 'toupload/' + filejpeg)
    except Exception as e:
        print(e)
