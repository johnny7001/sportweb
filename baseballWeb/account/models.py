""" from django.db import models

# Create your models here.
import requests
from bs4 import BeautifulSoup
import time
from lxml import html
import json
import csv
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.figure_factory as ff
from sklearn.preprocessing import LabelEncoder #載入標籤功能  #Label Encoding = 標籤編碼
import plotly.graph_objects as go

url = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2021&stats=season&group=hitting&gameType=R&limit=25&offset=0&sortStat=onBasePlusSlugging&order=desc"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
#headers 建立偽裝
resp = requests.get(url, headers=headers)
resp.encoding = "UTF-8"
time.sleep(5)
soup = BeautifulSoup(resp.text, "html5lib")
time.sleep(5)

a = resp.json()

dict_all = a["stats"]
print(type(dict_all))

playerName_List = [] #先建立清單
babip_List = []
for data in dict_all:
    playerName = playerName_List.append(data['playerName'])
    babip = babip_List.append(data['babip'])

dic = {'playerName': playerName_List, 'babip': babip_List}
labelencoder = LabelEncoder() #增加標籤
data = pd.DataFrame(dic)
data.to_csv('mlbTest.csv') #把資料寫入csv檔案

 """
