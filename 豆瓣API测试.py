import requests
# 测试豆瓣api
params = {'q': '云计算', 'tag': '', 'start': 0, 'count': 1}

r = requests.get('http://api.douban.com/v2/book/search', params=params)

# r.encodeing #编码信息
# 'utf-8'

print(r.json()['books'][0]["summary"])  # 网页内容
#
# 以下是requests库获取json信息
r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
# s=r.json()['data']['city']
# print(s)
