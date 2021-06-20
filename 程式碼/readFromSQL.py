import pymysql
import csv
import codecs

def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='npb_web', charset='utf8')
    return conn
def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()
def read_mysql_to_csv(filename):
    with codecs.open(filename=filename, mode='w+', encoding='utf8') as f:
        write = csv.writer(f)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'select * from team_data'
        results = query_all(cur, sql=sql, args=None)
        for result in results:
            print(result)
            write.writerow(result)

if __name__ == '__main__':
    read_mysql_to_csv('test002.csv')





