
import requests
from bs4 import BeautifulSoup

# スクレイピングしたいWebページのURL
url = "https://example.com"

# requestsモジュールを使用して、WebページのHTMLソースコードを取得
response = requests.get(url)

# BeautifulSoupを使用して、HTMLを解析
soup = BeautifulSoup(response.content, "html.parser")

# <div class="content font100">の中のテキストを取得
div_elements = soup.find_all("div", {"class": "content font100"})

# 取得したすべての<div>要素のテキストを出力
for div_element in div_elements:
    text = div_element.text.strip()
    print(text)
    
    
    ///////////////////////////
