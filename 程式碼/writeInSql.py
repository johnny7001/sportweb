import pymysql
import pandas as pd
import codecs #編碼器
import csv


# db = pymysql.connect(host="localhost", user="root", passwd="root", db="npb_web", charset="utf8mb4") #連線資料庫
# cursor = db.cursor() #建立游標連結
# sql = """CREATE TABLE team_data (
#         チーム VARCHAR(100),
#         防御率 VARCHAR(100),
#         試合 VARCHAR(100),
#         勝利 VARCHAR(100),
#         敗北 VARCHAR(100),
#         セブ VARCHAR(100),
#         ホル VARCHAR(100),
#         ＨＰ VARCHAR(100),
#         完投 VARCHAR(100),
#         完封勝 VARCHAR(100),
#         無四球 VARCHAR(100),
#         勝率 VARCHAR(100),
#         打者 VARCHAR(100),
#         投球回 VARCHAR(100),
#         安打 VARCHAR(100),
#         本塁打 VARCHAR(100),
#         四球 VARCHAR(100),
#         死球 VARCHAR(100),
#         故意四 VARCHAR(100),
#         三振 VARCHAR(100),
#         暴投 VARCHAR(100),
#         ボク VARCHAR(100),
#         失点 VARCHAR(100)
#         )"""
# cursor.execute(sql)
# cursor.close()
# db.close()

def get_conn(): #取得連線
    conn = pymysql.connect(host="localhost", user="root", passwd="root", db="npb_web", charset="utf8mb4")
    return conn
def insert(cur, sql, args): #執行插入資料
    cur.execute(sql, args)
def read_csv_to_mysql(filename): #讀取csv
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader) #next:返回可跌代的值(可以用for迴圈的物件)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into team_data values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' \
              '%s, %s, %s, %s, %s, %s, %s)'
        for item in reader:
            if item[1] is None or item[1] == "": #item[1]作為唯一鍵, 不能null
                continue
            args = tuple(item)
            print(args)
            insert(cur, sql=sql, args=args)
        conn.commit()
        cur.close()
        conn.close()

if __name__=='__main__':
    read_csv_to_mysql('npbBatterData.csv')
