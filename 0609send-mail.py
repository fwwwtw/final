# 寄信可以附加檔案，多寫一個可以內鑲圖片的

import email.message
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Gmail SMTP 設定
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "fafa0130@gmail.com"  # ngshs01@gmail.com
app_password = "wxgn nlwn qolk fwmg"  # 請改成你自己的應用程式密碼 vvgy txxr bqcc nyox
receiver_email = "m11382014@gm2.nutn.edu.tw"

# 加入 HTML 內容，cid 對應圖片
html = '''
<h1>hello</h1>
<div> 這是 HTML 的內容</div>
<div style="color:red">紅色的字</div>
<img src="cid:meow_party">
'''
msg = MIMEMultipart()  # 使用多種格式所組成的內容
msg = MIMEMultipart('related')  # 重點：用 related 才能插入圖片
msg.attach(MIMEText(html, 'html', 'utf-8'))  # 加入 HTML 內容

# 內嵌圖片（inline）
with open('meow_party.gif', 'rb') as f:
    img_data = f.read()
    inline_img = MIMEImage(img_data)
    inline_img.add_header('Content-ID', '<meow_party>')
    inline_img.add_header('Content-Disposition', 'inline', filename='meow_party.gif')
    msg.attach(inline_img)

# 使用 python 內建的 open 方法開啟指定目錄下的檔案
with open(r'C:\Users\yc\Pictures\ID\meow_party.gif', 'rb') as file:
    img = file.read()
attach_file = MIMEApplication(img, Name='meow_party.gif')  # 設定附加檔案圖片
msg.attach(attach_file)

msg['Subject']='附件是一張搞笑的圖'
msg["From"]=sender_email  # 寄件人
msg["To"]='fafa0130@gmail.com'  # 收件人徐偉玲m11382014@gm2.nutn.edu.tw

smtp = smtplib.SMTP('smtp.gmail.com', 587)  # google mail 伺服器的 port
smtp.ehlo()
smtp.starttls()
smtp.login('fafa0130@gmail.com', 'wxgn nlwn qolk fwmg')
status = smtp.send_message(msg)
print(status)
smtp.quit()
print('✔️郵件已寄出')
