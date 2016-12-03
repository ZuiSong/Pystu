import requests
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('美团酒店数据.xlsx')
worksheet = workbook.add_worksheet()
n = 1

pageurl = 'http://hotel.meituan.com/changsha/jiudian'

while n <= 1000:

    html = requests.get(pageurl).text
    soup = BeautifulSoup(html, 'html.parser')
    hotels = soup.find_all("div", class_='hotel')

    for hotel in hotels:
        intro = hotel.find('div', class_='intro')
        link = intro.find('a')['href']
        name = intro.find('a').get_text()
        label = hotel.find('span', class_='star').get_text()
        localtion = hotel.find('span', class_='loc').get_text()

        worksheet.write(n, 0, name)
        worksheet.write(n, 1, label)
        worksheet.write(n, 2, localtion)
        worksheet.write(n, 3, link)

        print(link, name, label, localtion)

        roomlist = hotel.find_all('li', class_='deallist-li')

        roomdata = []

        for room in roomlist:
            roomtypename = room.find('a').get_text()
            roomprice = room.find(
                'span', class_='original original--price').get_text()
            roomdata.append(roomtypename + ':' + roomprice)
            print(roomtypename, roomprice)
        worksheet.write(n, 4, str(roomdata))
        n += 1
    pageurl = 'http://hotel.meituan.com' + \
        soup.find('li', class_='next').a['href']

workbook.close()
