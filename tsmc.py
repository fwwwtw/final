# 0609 看台積電股票有沒有漲

import requests
from bs4 import BeautifulSoup

url = 'https://tw.stock.yahoo.com/quote/2330'  # 台積電 yahoo 股市網址
headers = {"User-Agent": "Mozilla/5.0"}  # Yahoo 有時會擋無 user-agent 的 request
web = requests.get(url, headers=headers)  # 取得網頁內容
soup = BeautifulSoup(web.text, 'html.parser') # 轉換內容成 BeautifulSoup 物件

title = soup.find('h1')  # 取得網頁標題，找到 <h1> 的內容
a = soup.select('.Fz\\(32px\\)')[0]   # 取得即時股價 ( 需跳脫括號 )
b = soup.select('.Fz\\(20px\\)')[0]  # 取得漲跌幅 ( 需跳脫括號 )

s = ''  # 漲或跌的狀態

try:
    # 判斷是否為下跌 ( 紅字 )
    if soup.select('#main-0-QuoteHeader-Proxy .C\\(\\$c-trend-down\\)'):
        s = '-'
except:
    pass
try:
    # 判斷是否為上跌 ( 綠字 )
    if soup.select('#main-0-QuoteHeader-Proxy .C\\(\\$c-trend-up\\)'):
        s = '+'
except:
    pass

if s == '':
    s = '-'  # 平盤或無法判斷漲跌

# 印出結果
print(f'{title.get_text()} : {a.get_text()} ( {s}{b.get_text()})')