######################################################

import requests
from bs4 import BeautifulSoup

source = urllib.request.urlopen(url)
soup = BeautifulSoup(source,'lxml')


response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

######################################################

#tags=soup.find_all('img')
#print(tags)

for tag in tags:
    image_url = tag['src']
    image_name = os.path.join('images', os.path.basename(image_url))

    try:
        # Send a GET request to the image URL
        response = requests.get(image_url, stream=True)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a local file with write-binary mode
            with open(image_name, 'wb') as file:
                # Iterate over the content of the response and write it to the local file
                for chunk in response.iter_content(chunk_size=128):
                    file.write(chunk)

            print(f"Image '{image_name}' saved successfully.")
        else:
            print(f"Failed to download image from '{image_url}'. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error downloading image from '{image_url}': {e}")

######################################################

from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd
import numpy as np
import os

######################################################

url = 'https://www.youtube.com/watch?v=5maOGFpd454'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# タイトルタグを取得
title = soup.find('meta', property='og:title')['content']
print(title)


######################################################

url = 'https://www.youtube.com/watch?v=5maOGFpd454'
source = urllib.request.urlopen(url)
soup = BeautifulSoup(source,'lxml')

title = soup.find('meta', property='og:title')['content']
print(title)


######################################################

