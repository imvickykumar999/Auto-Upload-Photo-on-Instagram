import shutil, os
from PIL import Image

try:
    shutil.rmtree('config')
except Exception as e:
    print(e)

if not os.path.exists('toupload'):
  os.mkdir('toupload')
  print('\nThere is no photo in toupload folder !!!')

def make_square(im, min_size=256, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

from instabot import Bot
bot = Bot()

print('Photo should be SQUARE !!!')
link = 'https://github.com/imvickykumar999/Auto-Upload-Photo-on-Instagram'

user = input('Enter Username : ')
passwd = input('Enter Password : ')
bot.login(username = user, password = passwd)

for file in os.listdir('toupload'):
    try:
        file0 = file.split('.')[0]
        file1 = file.split('.')[1]

        img = Image.open('toupload/' + f'{file0}.{file1}')
        rgb_img = img.convert('RGB')

        filepng =  'toupload/' + file0 + '.png'
        rgb_img.save(filepng)

        test_image = Image.open(filepng)
        new_image = make_square(test_image)
        new_image.save(filepng)

        img = Image.open(filepng)
        rgb_img = img.convert('RGB')

        filepng =  'toupload/' + file0 + '.jpeg'
        rgb_img.save(filepng)

        bot.upload_photo(filepng,
        caption = filepng + f' has been upload using {link}')

        if os.path.exists(filepng + '.REMOVE_ME'):
            os.remove(filepng + '.REMOVE_ME')

        if os.path.exists(file0 + '.png'):
            os.remove(file0 + '.png')

    except Exception as e:
        print(e)
