import requests
from bs4 import BeautifulSoup


url = "https://oz.by/people/more902677.html"
css_class = "item-type-card__title"

def trade_spider():
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    empty = []

    for link in soup.find_all("p", {'class': css_class}):
        empty.append(link.string)
    
    empty_set = set(empty)

    for i in empty_set:
        print(i)


trade_spider()