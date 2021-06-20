import requests
from bs4 import BeautifulSoup
import time
import lxml
url = 'https://tw.sports.yahoo.com/npb/'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
        #headers 建立偽裝
resp = requests.get(url, headers=headers)
resp.encoding = "UTF-8"
time.sleep(5)
soup = BeautifulSoup(resp.text, "lxml")
news_title = soup.find_all('h3', class_='Mb(5px)')
# news_url = soup.find_all('a', class_="ie-7_D(b)")
url_list1 = []
title_list1 = []
for item in news_title:
    title_list1.append(item.a.text.replace(u'\u3000', u''))
    url_list1.append(item.a.get('href'))
print(url_list1)
print(title_list1)





# print(title.parent.text)
# print(soup.find('a', class_="Fw(b) Td(n) C(#fff) C(#fff):h").get('href'))


