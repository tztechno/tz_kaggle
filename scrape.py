import requests
from bs4 import BeautifulSoup

source = urllib.request.urlopen(url)
soup = BeautifulSoup(source,'lxml')


response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
