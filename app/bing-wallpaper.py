#!../venv/bin/python3

from pathlib import Path
import requests
import json

NUM_OF_PHOTOS = 8
URL_BASE = 'http://www.bing.com'
URL_REQUEST = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n={}&mkt=en-US'.format(NUM_OF_PHOTOS)
PATH_WALLPAPERS = Path.home() / 'bing-wallpaper'
JSON_FILE = PATH_WALLPAPERS / 'updates.json'

# dict
response_dict = requests.get(URL_REQUEST)
data = response_dict.json()

# Записать ответ в json-файл
with open(JSON_FILE, 'w') as file_updates:
    json.dump(data, file_updates, indent=2)

# Забрать ссылку, сделать запрос, сохранить файл
for index in range(NUM_OF_PHOTOS):
    url = data['images'][index]['url']
    response_file = requests.get(URL_BASE + url)

    # Сохранить .jpg
    with open(PATH_WALLPAPERS.joinpath(str(index) + '.jpg'), 'wb') as file_jpg:
        file_jpg.write(response_file.content)
