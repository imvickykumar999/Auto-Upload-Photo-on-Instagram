
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

user = 'vix.bot'
passwd = getpass.getpass('\nEnter Instagram Password : ')

API_Key = getpass.getpass('Enter API key : ')
openai.api_key = API_Key

print('\nUploading ...')
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                messages=[{"role": "user", 
                           "content": "Trending Minecraft Games"}])

topics = completion.choices[0].message.content

try:
    topic = random.choice(topics.split('\n')[2:-2]).split('. ')[1]
except:
    topics = '''1. Minecraft 1.17: Caves and Cliffs Update - This upcoming update to Minecraft is highly anticipated by players. It introduces new underground features, biomes, mobs, and blocks, enhancing the exploration and mining experience.

2. Minecraft Dungeons - This spin-off game combines the Minecraft universe with action-packed dungeon crawling gameplay. Players can team up with friends to defeat mobs and bosses, collect gear, and explore various levels.

3. Minecraft Earth - A mobile augmented reality game that allows players to build and explore Minecraft creations in the real world. It incorporates real-world locations and encourages collaboration with other players.

4. Minecraft: Story Mode - Developed by Telltale Games, this episodic adventure game takes players on an interactive story-driven journey set in the Minecraft universe. Players make choices that affect the outcome and can shape the narrative.

5. Minecraft Education Edition - Designed for educational purposes, this version of Minecraft provides a platform for teachers to engage students in learning activities. It offers various features, including lesson plans, collaborative building, and coding exercises.

6. Minecraft Skyblock - This popular Minecraft game mode challenges players to survive on a floating island with limited resources. They must use their creativity and problem-solving skills to expand their island, gather resources, and survive.

7. Minecraft Bed Wars - A multiplayer game mode where players compete to destroy each other's beds while defending their own. It requires strategic planning, teamwork, and quick reflexes to outsmart opponents and emerge victorious.

8. Minecraft Survival Games - Inspired by the "Hunger Games" series, this game mode throws players into a map where they must scavenge for weapons and armor, eliminate opponents, and be the last one standing.

9. Minecraft Hypixel - Hypixel is a popular Minecraft server that offers a wide range of custom mini-games, including Bed Wars, Skyblock, and Survival Games. It attracts a large player base due to its diverse and engaging gameplay options.

10. Minecraft Creative Mode - Although not new, Minecraft's Creative Mode remains a favorite among players. It allows them unlimited resources, the ability to fly, and the freedom to create and build whatever they imagine in the game.
'''
    topic = random.choice(topics.split('\n')[2:-2]).split('. ')[1]

n=1
image_resp = openai.Image.create(prompt=topic, n=n, size="512x512")
file = time.time()

for i in range(n):
    img = list(image_resp['data'][i].values())[0]
    r = requests.get(img, allow_redirects=True)
    open(f'images/{file}.jpg', 'wb').write(r.content)

bot = Bot()
bot.login(username = user, password = passwd)

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

cap = f'🔥 This is Trending Video-Game image of "{topic}", created by OpenAI API and uploaded at {file} (unix time) using InstaBot package written in Python Language. #imvickykumar999 @minecraft 💡' 
bot.upload_photo(path, caption = cap)
