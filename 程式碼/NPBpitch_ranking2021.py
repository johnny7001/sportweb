from bs4 import BeautifulSoup
import requests
import pymysql
import csv
import lxml
import time
url = "https://npb.jp/bis/2021/stats/pit_c.html"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8" #編碼
time.sleep(5) #設定睡眠時間避免爬取時間太頻繁
# print(resp) #type = <class 'requests.models.Response'>
# print(resp.text) #得到html網頁碼
# print("____________________________________________________")
soup = BeautifulSoup(resp.text, "lxml") #使用lxml解析數據
# print(soup.text) #呈現文字 type = str
# print(type(soup.text))
tag_alltitle = soup.find_all("h2")

alltitle = [] #3個table的標題塞進List
# print(tag_alltitle) #type = <class 'bs4.element.ResultSet'>
for item in tag_alltitle:
    # print(i, end=" ")
    # print(i.text)
    alltitle.append(item.text)
# print(alltitle) #type = list
# print(type(alltitle))
# print(alltitle[0].strip()) #type = str, strip() = 去除空格,跳行...
# print(type(alltitle[0]))
tag_column = soup.find_all("tr")[1] #找到位置1的tr
# print(tag_column.text) #type = str
tag_columnList = []
for column in tag_column:
    # print(column.text.replace(u'\u3000', u'')) #去空格
    tag_columnList.append(((column.text.replace(u'|', u'')).replace(" ", "")).replace(u'\u3000', u'').replace("｜", ""))
del tag_columnList[15]
print(tag_columnList) #將全部的column塞到list裡面, len=25

pitchList1 = [] #投手成績(規定投球回以上)的選手list
tag_pitch1 = soup.find_all("tr")[2:15] #位置2~15為選手資料
for pitch1 in tag_pitch1: #len(pitch) = 27
    pitchList1_data = []#每位選手資料
    pitch1.text.replace(u'\u3000', u'') #type = str
    for td in pitch1:
        pitchList1_data.append(td.text.replace(u'\u3000', u''))
    # print()
    pitchList1_data[15] = pitchList1_data[15] + pitchList1_data[16]
    del pitchList1_data[16]
    pitchList1.append(pitchList1_data)
print(pitchList1) #len = 13
print(len(pitchList1[0]))
# db = pymysql.connect(host="localhost", user="root", passwd="root", db="npb_data", charset="utf8mb4") #連線資料庫
# cursor = db.cursor()
#
# # def npb_pitch_column():
# #     for clm in range(len(tag_columnList)): #將欄位名稱插入資料庫
# #         return tag_columnList[clm]
#     # sql = """alter table pitch_ranking_player add `%s` VARCHAR(50)""" #注意 %s 要加 ` 符號
#     # sql = sql.format(tag_columnList[clm])
#     # cursor.execute(sql, tag_columnList[clm])
# # db.commit()
# # db.close()
#
#
#
# for item in range(len(pitchList1)):
#     # print(pitchList1[item])
#     sql = """insert into pitch_ranking_player(`'順位'`, `'投手'`, 隊伍, `'防御率'`, `'登板'`, `'勝利'`, `'敗北'`, `'セブ'`,
#     `'ホル'`, `'ＨＰ'`, `'完投'`, `'完封勝'`,`'無四球'`, `'勝率'`, `'打者'`, `'投球回'`, `'安打'`, `'本塁打'`, `'四球'`, `'故意四'`
#     , `'死球'`, `'三振'`, `'暴投'`, `'ボク'`, `'失点'`, `'自責点'`) values (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#     sql = sql.format(pitchList1[item][0], pitchList1[item][1], pitchList1[item][2], pitchList1[item][3],
#                      pitchList1[item][4], pitchList1[item][5], pitchList1[item][6], pitchList1[item][7],
#                      pitchList1[item][8], pitchList1[item][9], pitchList1[item][10], pitchList1[item][11],
#                      pitchList1[item][12], pitchList1[item][13], pitchList1[item][14], pitchList1[item][15],
#                      pitchList1[item][16], pitchList1[item][17], pitchList1[item][18], pitchList1[item][19],
#                      pitchList1[item][20], pitchList1[item][21], pitchList1[item][22], pitchList1[item][23],
#                      pitchList1[item][24], pitchList1[item][25])
#
#     cursor.execute(sql, pitchList1[item])
# db.commit()
# db.close()
# sql = """insert into pitch_ranking_player('順位', '投手', '防御率', '登板', '勝利', '敗北', 'セブ', 'ホル', 'ＨＰ', '完投', '完封勝',
#     '無四球', '勝率', '打者', '投球回', '安打', '本塁打', '四球', '故意四', '死球', '三振', '暴投', 'ボク', '失点', '自責点') values (%s, %s, %s, %s, %s,
#      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""


