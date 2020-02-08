import bs4
import urllib.request

url = "https://search.shopping.naver.com/search/all.nhn?query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%87%BC%ED%95%91&frm=NVSCPRO"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, "html.parser")
items = soup.find('ul', {"class": "goods_list"}).find_all('ul', {"class": "goods_list"})
for item in items:
    tmp = item.find('div', {"class": "info"})
    print(tmp)


