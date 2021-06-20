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
import lxml

url = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2021&sportId=1&stats=season&group=pitching&gameType=R&offset=0&sortStat=earnedRunAverage&order=asc"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
#headers 建立偽裝
resp = requests.get(url, headers=headers)
resp.encoding = "UTF-8"
time.sleep(5)

soup = BeautifulSoup(resp.text, "lxml")
a = resp.json()
# print(a) #type = dict
dict_all = a["stats"]

playerName_List = []
strikeoutsPer9_List = []
baseOnBallsPer9_List = []
hitsPer9_List = []
homeRunsPer9_List = []
strikesoutsToWalks_List = []

for data in dict_all:
    playerName = playerName_List.append(data['playerName'])
    strikeoutsPer9 = strikeoutsPer9_List.append(data['strikeoutsPer9'])
    baseOnBallsPer9 = baseOnBallsPer9_List.append(data['baseOnBallsPer9'])
    homeRunsPer9 = homeRunsPer9_List.append(data['homeRunsPer9'])
    strikesoutsToWalks = strikesoutsToWalks_List.append(data['strikesoutsToWalks'])
    hitsPer9 = hitsPer9_List.append(data['hitsPer9'])

trace1 = go.Scatter(x=playerName_List,
                    y=strikeoutsPer9_List, name="strikeoutsPer9", connectgaps=True)
trace2 = go.Scatter(x=playerName_List,
                    y=baseOnBallsPer9_List, name="baseOnBallsPer9")
# trace3 = go.Scatter(x=playerName_List,
#                     y=homeRunsPer9_List, name="homeRunsPer9", connectgaps=True)
# trace4 = go.Scatter(x=playerName_List,
#                     y=strikesoutsToWalks_List, name="strikesoutsToWalks", connectgaps=True)
# trace5 = go.Scatter(x=playerName_List,
#                     y=hitsPer9_List, name="hitsPer9")
data = [trace1, trace2]

# print(type(data)) #type = list

py.plot(data, filename="mlbPitcherMix01.html")
