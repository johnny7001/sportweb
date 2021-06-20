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
# print(dict_all[0])

playerName_List = []
teamAbbrev_List = [] #球隊名稱簡稱
wins_List = [] #勝投
losses_List = [] #敗投
era_List = [] #防禦率(自責分率, 每一場平均會失分)
gamesPitched_List = [] #出賽
gamesStarted_List = [] #先發
completeGames_List = [] #完投
shutouts_List = [] #完封
saves_List = [] #救援成功
saveOpportunities_List = [] #救援機會
inningsPitched_List = [] #投球局數
hits_List = [] #被安打
runs_List = [] #失分
earnedRuns_List = [] #自責分
homeRuns_List = [] #被全壘打
baseOnBalls_List = [] #四死球
strikeOuts_List = [] #三振
whip_List = [] #每局被上壘率
avg_List = [] #打擊率
hitByPitch_List = [] #觸身球
#
for data in dict_all:
    playerName = playerName_List.append(data['playerName'])
#     teamAbbrev = teamAbbrev_List.append(data['teamAbbrev'])
#     wins = wins_List.append(data['wins'])
#     losses = losses_List.append(data['losses'])
#     era = era_List.append(data['era'])
#     gamesPitched = gamesPitched_List.append(data['gamesPitched'])
#     gamesStarted = gamesStarted_List.append(data['gamesStarted'])
#     completeGames = completeGames_List.append(data['completeGames'])
#     shutouts = shutouts_List.append(data['shutouts'])
#     saves = saves_List.append(data['saves'])
#     saveOpportunities = saveOpportunities_List.append(data['saveOpportunities'])
#     inningsPitched = inningsPitched_List.append(data['inningsPitched'])
#     hits = hits_List.append(data['hits'])
#     runs = runs_List.append(data['runs'])
#     earnedRuns = earnedRuns_List.append(data['earnedRuns'])
#     homeRuns = homeRuns_List.append(data['homeRuns'])
    baseOnBalls = baseOnBalls_List.append(data['baseOnBalls'])
    strikeOuts = strikeOuts_List.append(data['strikeOuts'])
#     whip = whip_List.append(data['whip'])
#     avg = avg_List.append(data['avg'])
#     hitByPitch = hitByPitch_List.append(data['hitByPitch'])

# df = pd.read_csv('mlbPitcher.csv')
#
# table = ff.create_table(df)
# # table.update_layout(width=500, height=300)
# # table.layout.columns_width = 100
# py.plot(table, filename='mlbDict.html')

trace1 = go.Scatter(x=playerName_List,
                    y=strikeOuts_List, name="strikeOuts", connectgaps=True)
trace2 = go.Scatter(x=playerName_List,
                    y=baseOnBalls_List, name="baseOnBalls")
data = [trace1, trace2]

# print(type(data)) #type = list
fig = dict(data=data)
py.plot(data, filename="mlbPitcherSO_BB.html")



# b = dict_all[0]
# print(type(dict_all[0])) #type = dict
# print(b.keys()) #抓取key
# print(type(b.keys()))
# print(b.values()) #抓取values
# print(type(b.values()))
# print(b.items())

#
# dic = {'playerName': playerName_List, 'teamAbbrev': teamAbbrev_List, 'wins': wins_List,
#        'losses': losses_List, 'era': era_List, 'gamesPitched': gamesPitched_List, 'gamesStarted': gamesStarted_List,
#        'completeGames': completeGames_List, 'shutouts': shutouts_List, 'saves': saves_List,
#        'saveOpportunities': saveOpportunities_List, 'inningsPitched': inningsPitched_List, 'hits': hits_List,
#        'runs': runs_List, 'earnedRuns': earnedRuns_List, 'homeRuns': homeRuns_List, 'baseOnBalls': baseOnBalls_List,
#        'strikeOuts': strikeOuts_List, 'whip': whip_List, 'avg': avg_List, 'hitByPitch': hitByPitch_List}
# labelencoder = LabelEncoder() #增加標籤
# dict = pd.DataFrame(dic)
# dict.to_csv('mlbDict.csv') #把資料寫入csv檔案


