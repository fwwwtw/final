# 0609 統一發票兌獎系統

import requests
from bs4 import BeautifulSoup

url = 'https://invoice.etax.nat.gov.tw/index.html'

try:
    web = requests.get(url, timeout=10)  # 取得網頁內容+增加 timeout 避免永久卡住
    web.raise_for_status()  # 如果 HTTP 回應馬不是 200，會拋出錯誤
    web.encoding = 'utf-8'  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
    print(web.text)
    soup = BeautifulSoup(web.text, 'html.parser')
    td = soup.select('.container-fluid')[0].select('.etw-tbiggest') # 中獎號碼位置
    ns = td[0].getText()     # 特別獎號碼
    n1 = td[1].getText()     # 特獎號碼
    n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] # 頭獎號碼
    
    while True:
        try:
            num = input("請輸入發票號碼 (或輸入q離開): ")
            if num.lower() == 'q':
                print("結束兌獎程式")
                break
            if num == ns:
                print("🎉 恭喜！您的發票號碼中得特別獎 1000 萬元！")
            elif num == n1:
                print("🎉 恭喜！您的發票號碼中得特獎 200 萬元！")
            else:
                match = False
                for i in n2:
                    if num == i:
                         print('🎉 對中頭獎 20 萬元 !')
                         matched = True
                         break
                    elif num[-7:] == i[-7:]:
                        print("🎉 恭喜！您的發票號碼中得二獎 4 萬元！")
                        match = True
                        break
                    elif num[-6:] == i[-6:]:
                        print("🎉 恭喜！您的發票號碼中得三獎 1 萬元！")
                        match = True
                        break
                    elif num[-5:] == i[-5:]:
                        print("🎉 恭喜！您的發票號碼中得四獎 4 千元！")
                        match = True
                        break
                    elif num[-4:] == i[-4:]:
                        print("🎉 恭喜！您的發票號碼中得五獎 1 千元！")
                        match = True
                        break
                    elif num[-3:] == i[-3:]:
                        print("🎉 恭喜！您的發票號碼中得六獎 2 百元！")
                        match = True
                        break
                if not matched:
                    print('🥹很抱歉，未中獎。')
        except:
            print('⚠️ 輸入錯誤，請重新輸入發票號碼。')
except requests.exceptions.RequestException as e:
    print('🚫 無法連線至電子發票網頁。請檢察網路連線或稍後再試。')
    print(f'詳細錯誤: {e}')