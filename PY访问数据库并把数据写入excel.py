# python3.5
# 写入excel示例
# 访问数据库
# encoding=utf-8
import pymysql
import xlsxwriter
workbook = xlsxwriter.Workbook('豆瓣图书排行榜.xlsx')
worksheet = workbook.add_worksheet('豆瓣图书')
conn = pymysql.connect(user='root', passwd='123',
                       host='127.0.0.1', db='mybatis', charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM douban_movie_book")
row = 0
for r in cur:
    colum = 0
    while colum < len(r):
        worksheet.write(row, colum, r[colum])
        colum = colum + 1
    row = row + 1
cur.close()
conn.close()
workbook.close()
