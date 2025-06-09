# app.py - 期末要做 Flask 主頁整合介面
# 05/26 自己做一個網站, 搭配Procfile / requirements.txt
# 網頁開Render: https://dashboard.render.com/web/srv-d0q04k6mcj7s73ejeu60
# GitHub: https://github.com/fwwwtw/flask

from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import os

app = Flask(__name__)  # __name__代表目前執行的模組
app.secret_key = "apple123banana456"  # 我隨便設的字串因為我怕被亂改

# 要進行編輯的 .py 腳本清單
EDITABLE_SCRIPTS = [
    "cctv.py",
    "tsmc.py",
    "0609send-mail.py",
    "currency-rate.py",
    "invoice_check.py"
]

@app.route("/")  # 函式的裝飾 (Decorator): 以函式為基礎，提供附加功能
def index():
    return render_template("index.html", scripts=EDITABLE_SCRIPTS)

@app.route("/edit/<script>", methods=["GET", "POST"])
def edit(script):
    if script not in EDITABLE_SCRIPTS:
        return "⚠️ 檔案不可編輯", 403  # 網頁會顯示
    script_path = os.path.join(os.getcwd(), script)
    if request.method == "POST":
        code = request.form.get("code", "")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(code)
        flash(f"{script} 已儲存！")
        return redirect(url_for("edit", script=script))
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        code = ""
        flash(f"讀取檔案錯誤：{e}")
    return render_template("edit.html", script=script, code=code)

@app.route("/run/<script>", methods=["POST"])
def run_script(script):
    if script not in EDITABLE_SCRIPTS:
        return "⚠️ 檔案不可執行", 403
    try:
        result = subprocess.run(["python", script], capture_output=True, text=True, timeout=30)
        output = result.stdout + "\n" + result.stderr
    except Exception as e:
        output = f"執行時發生錯誤：{e}"
    return render_template("result.html", script=script, output=output)

if __name__ == "__main__":  # 如果以主程式執行
    app.run(debug=True)  # 立刻啟動伺服器
