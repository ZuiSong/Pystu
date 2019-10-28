# encoding=utf-8
import requests
# 测试豆瓣api
params = {'param': '送子观音', 'email': '378818573@qq.com'}
header = {
    # 'Referer': 'http://login.sina.com.cn/crossdomain2.php?action=login&entry=qq&r=https%3A%2F%2Fpassport.weibo.com%2Fwbsso%2Flogin%3Fssosavestate%3D1508218359%26url%3Dhttp%253A%252F%252Fweibo.com%252F%253Fsudaref%253Dgraph.qq.com%26ticket%3DST-MzM0OTg5Njk3NA%3D%3D-1476682359-gz-FFDF83371860AAD82688210C42A02843%26retcode%3D0',
    'host': 'weibo.com',
    'cookie': 'YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; login_sid_t=e8d1730883de0ad680187f09aa040f3d; YF-V5-G0=16139189c1dbd74e7d073bc6ebfa4935; _s_tentry=-; YF-Page-G0=416186e6974c7d5349e42861f3303251; Apache=9770627937575.113.1476682341829; SINAGLOBAL=9770627937575.113.1476682341829; ULV=1476682341836:1:1:1:9770627937575.113.1476682341829:; SSOLoginState=1476682371; SUB=_2A251ABLTDeTxGeVN71sZ-SjFzDiIHXVWdAMbrDV8PUNbmtBeLVn8kW9oR0Wzvpsdq1-6Bjo3N8OWRMgaTg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Why2husHh2SOfAxk6ujadQz5JpX5KzhUgL.Foe0Sh.R1Kq4S0B2dJLoIpxSxCH81C-RSb-R1CH8SCHFSCHW1Btt; SUHB=0BLYZlimCUJITm; ALF=1508218359; wvr=6; UOR=www.anjian.com,widget.weibo.com,graph.qq.com; WBStorage=86fb700cbf513258|undefined',
    'User-Agent': 'Mozilla / 5.0 (Windows NT 6.3\
                                   Win64\
                                   x64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 54.0.2840.59 Safari / 537.36'
}
# for x in range(1,11):
r = requests.get(
    'http://weibo.com/zuisong/home?wvr=5&sudaref=graph.qq.com', headers=header)
print(r.url)
print(r.text)
