import pymysql
from urllib import request
conn = pymysql.connect(user='root', passwd='123',
                       host='127.0.0.1', db='mybatis', charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM douban_movie_book")
i = 1
for r in cur:
    # 下载电影封面
    try:
        print(r[1])
        request.urlretrieve(r[3], 'D:\\test\\%s.jpg' % r[1])
    except:
        print('漏掉1张封面')
        continue
    i = i + 1
cur.close()
conn.close()
