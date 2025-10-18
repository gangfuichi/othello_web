from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# ブラウザを開いたときだけ記録
def log_access(ip):
    time = datetime.datetime.now()
    with open("access_log.txt", "a") as f:
        f.write(f"{time} {ip} accessed\n")

@app.route("/")
def index():
    user_ip = request.remote_addr
    log_access(user_ip)
    return render_template("index.html")  # オセロページを表示

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)  # 自分のPC用