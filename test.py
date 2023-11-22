import json
from requests_html import HTMLSession
from requests_html import UserAgent
with open('cookie.txt', 'r') as f:
    cookies = f.read()
s = HTMLSession()
ua = UserAgent().random
d_cookies = {}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    d_cookies[key] = value
url = ('https://wkrtcs.bdimg.com/rtcs/getbdjson?bucketNum=70&pn=1&rn=5&range=75931-23808_23809-44453_44454-62310_62311'
       '-75930_75931-&rsign=p_5-r_0-s_c26ca&dataType=rtcs&md5sum=57c4668f9fad97f2d69c795041aebcd3&sign=77926bef34'
       '&rtcs_flag=1&rtcs_ver=4.1&callback=sf_edu_wenku_rtcs_doc_jsonp_1_5&_=1700566896520')
headers = {'User-Agent': ua}
response = s.get(url=url, cookies=d_cookies, headers=headers).text
# with open('json.txt','w') as f:
#     f.write(response)
count = 0
for i in range(100):
    if response[i] == '{':
        count = i
        break
response = response[count:-1:1]
js = json.loads(response)
js = js["document.xml"]
# print(js[0]['c'][1]['c'])
ans = ''
for i in js[0:len(js)]:
    for j in i['c']:
        for k in j['c']:
            ans += k['c']
        ans += '\n'
print(ans)
