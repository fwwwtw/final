# app.py - 期末要做 Flask 主頁整合介面
# 05/26 自己做一個網站, 搭配Procfile / requirements.txt
# 網頁開Render: https://dashboard.render.com/web/srv-d0q04k6mcj7s73ejeu60
# GitHub: https://github.com/fwwwtw/flask

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)  # __name__代表目前執行的模組
app.secret_key = "apple123banana456"  # 我隨便設的字串因為我怕被亂改

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    cctv_info = ""
    if request.method == 'POST':
        action = request.form.get('action')
        script_map = {
            'currency': 'currency-rate.py',
            #'invoice': 'invoice_check.py',
            'tsmc': 'tsmc.py',
            #'cctv': 'cctv.py',
            'mail': '0609send-mail.py'
        }
        script = script_map.get(action)
        if script == 'cctv.py':
            cctv_info = "⚠️ CCTV 影像僅支援本機執行，無法於 Render 網頁中顯示（請在自己的電腦執行 cctv.py 觀看即時畫面）。"
        elif script:
            try:
                # 執行 Python 腳本，抓 stdout/err
                result = subprocess.run(['python', script], capture_output=True, text=True, timeout=60)
                output = result.stdout + '\n' + result.stderr
            except Exception as e:
                output = f"⚠️ 執行 {script} 時發生錯誤：\n{e}"
    return render_template('index.html', output=output, cctv_info=cctv_info)

if __name__ == "__main__":  # 如果以主程式執行
    app.run(debug=True)  # 立刻啟動伺服器
