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
import matplotlib.pyplot as plt
import plotly.express as px

years_List = []
LionAvg_list = []
SoftbankAvg_list = []
RakutenAvg_list = []
HamAvg_list = []
MarinesAvg_list = []
OrixAvg_list = []

for years in range(2021, 2022):
    url = "https://npb.jp/bis/" + str(years) + "/stats/tmp_p.html"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
    #headers 建立偽裝
    resp = requests.get(url, headers=headers)
    resp.encoding = "UTF-8"
    time.sleep(5)
    soup = BeautifulSoup(resp.text, "lxml")
    TeamRank_List = [] #球隊排行清單
    Team_List = []  #各球隊清單
    for tr in soup.select('tr')[1:-1]:
        # print(tr)
        Team_List = []
        count = 0
        for td in tr:
            if count == 24:
                break
            else:
                Team_List.append(td.text.replace(u'|', u'').replace(" ", "").replace(u'\u3000', u'').replace("｜", ""))
                count += 1
        TeamRank_List.append(Team_List)
    # print(years, TeamRank_List)
    columns = soup.select('tr')[0]
    columns_List = [] #標題欄位
    for column in columns:
        columns_List.append(column.text.replace(u'|', u'').replace(" ", "").replace(u'\u3000', u'').replace("｜", ""))

    table = [] #結合完column跟data的list
    for data in TeamRank_List:
        TeamRank = dict(zip(columns_List, data))
        table.append(TeamRank)

    for team in TeamRank_List:
        if '西武' in team:
            # print(int(team[1].replace(".", "")) / 1000)
            LionAvg_list.append(int(team[1].replace(".", "")) / 1000)
        if 'ソフトバンク' in team:
            # print(int(team[1].replace(".", "")) / 1000)
            SoftbankAvg_list.append(int(team[1].replace(".", "")) / 1000)
        if '楽天' in team:
            RakutenAvg_list.append(int(team[1].replace(".", "")) / 1000)
        if '日本ハム' in team:
            # print(int(team[1].replace(".", "")) / 1000)
            HamAvg_list.append(int(team[1].replace(".", "")) / 1000)
        if 'オリックス' in team:
            # print(int(team[1].replace(".", "")) / 1000)
            OrixAvg_list.append(int(team[1].replace(".", "")) / 1000)
        if 'ロッテ' in team:
            MarinesAvg_list.append(int(team[1].replace(".", "")) / 1000)






# trace1 = go.Scatter(x=years_List,
#                     y=LionAvg_list, name="LionAvg", connectgaps=True, line=dict(color="#2828FF"))
# trace2 = go.Scatter(x=years_List,
#                     y=SoftbankAvg_list, name="SoftbankAvg", line=dict(color="#FFDC35"))
# trace3 = go.Scatter(x=years_List,
#                     y=RakutenAvg_list, name="RakutenAvg", line=dict(color="#FF0000"))
# trace4 = go.Scatter(x=years_List,
#                     y=HamAvg_list, name="HamAvg", line=dict(color="#2894FF"))
# trace5 = go.Scatter(x=years_List,
#                     y=OrixAvg_list, name="OrixAvg", line=dict(color="#E1E100"))
# trace6 = go.Scatter(x=years_List,
#                     y=MarinesAvg_list, name="MarinesAvg", line=dict(color="#272727"))
#
#
# data = [trace1, trace2, trace3, trace4, trace5, trace6]
# py.plot(data, filename="npbTeamPitcher_avg.html")





