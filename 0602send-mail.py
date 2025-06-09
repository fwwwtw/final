# 0602 郵件編輯器? 自己去google應用程式密碼抓密碼wxgn nlwn qolk fwmg

import email.message
import smtplib

# Gmail SMTP 設定
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "fafa0130@gmail.com"  # ngshs01@gmail.com
app_password = "wxgn nlwn qolk fwmg"  # 請改成你自己的應用程式密碼vvgy txxr bqcc nyox

# 寄送 Email 的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]=sender_email  # 寄件人
msg["To"]='fafa0130@gmail.com'  # 收件人m11382014@gm2.nutn.edu.tw
msg["Subject"]='你好'
# 寄送純文字內容
msg.set_content('老師說測試看看')

import smtplib
# 發送郵件
server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # "主機名稱", 連接負號
server.login(sender_email, app_password)  # "帳號", "密碼"
# msg 變數存放上一個步驟準備好的訊息物件
server.send_message(msg)
server.quit()
print('✔️郵件已寄出')
