# `Auto Upload Photo on` [`Instagram`](https://www.instagram.com/vix.bot/)
---------------------------------------

## >>> Instabot library is used.

![image](https://user-images.githubusercontent.com/50515418/129475280-4b56ad63-6257-4205-b689-277cf9e20b6a.png)

## >> Direction to use:
- Put all photos in toupload folder.
- Photo should be SQUARE (1:1 Aspect Ratio)
- run `python instaphoto.py`

---------------------------------------

### Output on cmd
    C:\Users\Vicky\Desktop\Projects\Package_python\python package\vixuploader\autouploadinsta>python instaphoto.py

    2021-08-15 15:41:28,200 - INFO - Instabot version: 0.117.0 Started
    Photo should be SQUARE !!!

    Enter Username : oye.vicks
    Enter Password : ********

    2021-08-15 15:41:30,668 - INFO - Not yet logged in starting: PRE-LOGIN FLOW!
    2021-08-15 15:41:34,652 - INFO - Logged-in successfully as 'oye.vicks'!
    2021-08-15 15:41:34,652 - INFO - LOGIN FLOW! Just logged-in: True
    FOUND: w:682 h:681 r:1.0014684287812041
    2021-08-15 15:42:18,856 - INFO - Photo 'toupload/galtaji.jpeg' is uploaded.
    FOUND: w:682 h:682 r:1.0
    2021-08-15 15:42:40,236 - INFO - Photo 'toupload/iskcon.jpeg' is uploaded.
    FOUND: w:681 h:681 r:1.0
    2021-08-15 15:43:06,380 - INFO - Photo 'toupload/tour.jpeg' is uploaded.
    2021-08-15 15:43:06,383 - INFO - Total requests: 37

----------------------------

# Instagram Message Bot

    from instabot import Bot
    bot = Bot()

    bot.login(username="Your Username", password="Your Password")
    bot.send_message("Hi Brother", ["Receiver's Username"])

--------------------------

# Download Reel Audio and Video

    import re

    reel_id = input('Enter reel link :')
    reel_id = list(reel_id.split('/'))

    if len(reel_id[4]) == 11:
        reel_id = reel_id[4]
    elif len(reel_id[5]) == 11:
        reel_id = reel_id[5]
    else:
        reel_id = 'CoT1MflIGJg' # default value if error.

    link = f'https://www.instagram.com/reel/{reel_id}/'
    dev_link = link + '?__a=1&__d=dis'
    print('\nClick below link ...')
    print(dev_link)

    dev_json = input('''

    1. Click above link
    2. Copy site content
    3. Paste below.

    ''')

    def reel_audio():
        a = re.search(r'\b(progressive_download_url)\b', dev_json)
        start_index = a.start()
        start_index = start_index + 3 + len('progressive_download_url')

        b = re.search(r'\b(duration_in_ms)\b', dev_json)
        end_index = b.start()
        end_index = end_index - 3

        audio_link = dev_json[start_index : end_index]
        print(audio_link)

    def reel_video():
        a = re.search(r'\b(-1.cdninstagram.com/o1/v/t16/f1/m82/)\b', dev_json)
        check_index = a.start()
        start_index = check_index - 21

        b = re.search(r'\b(-1.cdninstagram.com/o1/v/t16/f1/m82/)\b', dev_json[check_index:])
        end_index = b.start()
        end_index = end_index - 72
        end_index += start_index

        audio_link = dev_json[start_index : end_index]
        print(audio_link)

    import os
    os.system('cls')

    reel_audio()
    print()
    reel_video()
    
------------------------

### Output

Audio Link :  https://scontent-ams4-1.xx.fbcdn.net/v/t39.12897-6/310920570_1568464836890092_7375339126931823372_n.m4a?_nc_cat=110&ccb=1-7&_nc_sid=02c1ff&_nc_ohc=JsYnbF-rvLgAX_YhMcc&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent-ams4-1.xx&oh=00_AfArT_lBr0GRAyIQ8pw3nn4a_YVDNohwciqHfk9BPj9kRA&oe=63EAD3A0

Video Link :  https://scontent-ams2-1.cdninstagram.com/o1/v/t16/f1/m82/C649EC3D3C89CCD8207EC552A49EBF9B_video_dashinit.mp4?efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uNzIwLmNsaXBzLmJhc2VsaW5lIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=108&vs=549247196839797_775853929&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC9DNjQ5RUMzRDNDODlDQ0Q4MjA3RUM1NTJBNDlFQkY5Ql92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVABgkR0tFZE9nZEY5ZVVwb3ZJQ0FJQXJaUEZ0RjZBZGJwUjFBQUFGFQICyAEAKAAYABsAFQAAJtb3wZO9qOk%2FFQIoAkMzLBdAIap%2B%2Bdsi0RgSZGFzaF9iYXNlbGluZV8xX3YxEQB1%2FgcA&_nc_rid=608490cda0&ccb=9-4&oh=00_AfAoPmZ5FG3YcfOBsVzWnRvq4j0T2xe64udghlDBwTzbeA&oe=63E8626E&_nc_sid=74f7b
