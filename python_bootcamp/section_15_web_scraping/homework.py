import requests
import bs4

base_url = 'https://quotes.toscrape.com/page/{}/'

# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# authors = soup.select('.author')
# tags = soup.select('.tag-item')
# quotes = soup.select('.text')

# for quote in quotes:
#     print(quote.text)

# for tag in tags:
#     print(tag.text)

# for author in authors:
#     print(author.text)

iterator = 1
unique_authors = set()

while True:
    res = requests.get(base_url.format(iterator))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    authors = soup.select('.author')
    if not authors:
        break
    for author in authors:
        unique_authors.add(author.text)

    iterator += 1

for i in sorted(unique_authors):
    print(i)
