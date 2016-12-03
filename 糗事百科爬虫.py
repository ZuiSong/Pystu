# python3.5 爬虫教程
# 一个爬取糗事百科的爬虫
# 陈健
# 自动保存糗事百科文字内容到py所在文件夹的《糗事百科.xlsx》文件
import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter


def spider(weburl):
    workbook = xlsxwriter.Workbook('糗事百科.xlsx')
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
        eles = soup.find_all("div", class_="content")
        for ele in eles:
            worksheet.write(n, 0, ele.text.strip())
            n = n + 1
        try:
            weburl = 'http://www.qiushibaike.com' + \
                soup.find('span', class_='next').parent['href']
        except:
            print('结束了')
            break
spider("http://www.qiushibaike.com/text/")
