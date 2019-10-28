# encoding=utf-8
import requests
# 测试豆瓣api
data = {'name':'陈健', 'email':'378818573@qq.com'}
for x in range(1, 11):
	r = requests.post('http://127.0.0.1:8080/user/user/add', data=data)
# print(r.url)
# print(r.text,end='')
