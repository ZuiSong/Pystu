# python3.5 爬虫教程
# 一个简单豆瓣榜单的示例爬虫
# 陈健
# 自动保存榜单内容到py所在文件夹的xlsx文件
# encoding=utf-8
import urllib.request

from bs4 import BeautifulSoup
import xlsxwriter


def spider(weburl):
    workbook = xlsxwriter.Workbook('豆瓣.xlsx')
    worksheet = workbook.add_worksheet()
    n = 1
    while True:
        webheader = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=weburl, headers=webheader)
        webPage = urllib.request.urlopen(req)
        data = webPage.read()
        data = data.decode('UTF-8')
        soup = BeautifulSoup(data, 'html.parser')
        eles = soup.find_all("div", class_="bd doulist-subject")
        for ele in eles:
            ele = BeautifulSoup(str(ele), "html.parser")
            movieName = ele.find("div", class_='title').a.string.strip()
            worksheet.write(n, 0, str(movieName))
            doubanLink = ele.find("div", class_='title').a['href']
            worksheet.write(n, 1, str(doubanLink))
            movieGrade = ele.find('span', class_='rating_nums').string
            src = ele.find('img')['src']
            worksheet.write(n, 2, str(src))
            worksheet.write(n, 3, float(movieGrade))
            info = ele.find('div', class_='abstract').text.replace(
                " ", "").strip()
            worksheet.write(n, 4, str(info))
            n = n + 1
            print(movieName, '评分:' + movieGrade)
        try:
            weburl = soup.find('link', rel='next')['href']
        except:
            print('结束了')
            break

spider("https://www.douban.com/doulist/240962/?start=0&sort=seq&sub_type=")
