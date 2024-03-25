
import requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')

import pandas as pd
df = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Stick Maker']],
columns=['id','name', 'occupation'])
print(df)
df = pd.read_csv('WHR_2019.csv')

import numpy as np

c = np.array([1, 2, 3])
print(c)
d = np.array([[1, 2], [3, 4]])
print(np.cos(d))
a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)
print(b)
print(np.matmul(a, b))

import matplotlib.pyplot as plt
labels = ['2017', '2018', '2019', '2020', '2021']
android_users = [85, 80, 75, 69.2, 91]
ios_users = [15.0, 20.0, 25.0, 30.8, 9.0]
width = 0.35
fig, ax = plt.subplots()
ax.bar(labels, android_users, width, label='Android')
ax.bar(labels, ios_users, width, bottom=android_users,
      label='iOS')
ax.set_ylabel('Соотношение, в %')
ax.set_title('Распределение устройств на Android и iOS')
ax.legend(loc='lower left', title='Устройства')
plt.show()

from PIL import Image, ImageDraw
image = Image.open('image-pillow.png')
image.show()

img = Image.new('RGBA', (200, 200), 'white')
idraw = ImageDraw.Draw(img)
idraw.rectangle((10, 10, 100, 100), fill='blue')
img.show()