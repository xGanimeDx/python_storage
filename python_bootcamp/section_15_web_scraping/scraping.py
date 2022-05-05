import requests
import bs4

# NOTE: #1
# url = 'https://en.wikipedia.org/wiki/Grace_Hopper'
# result = requests.get("http://www.example.com")
# soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup.select('title')[0].getText())

# NOTE: #2
# res = requests.get(url)
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# for item in soup.select('.toctext'):
#     print(item.text)

# NOTE: #3
url = 'https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup.select('.thumbimage'))
image = soup.select('.thumbimage')[1]
image_link = requests.get(f'https:{image["src"]}')
f = open('python_bootcamp/section_15_web_scraping/iamge.jpg', 'wb')
f.write(image_link.content)
f.close()
