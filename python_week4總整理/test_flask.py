# 步驟1：導入 Flask
from flask import Flask

# 步驟2：建立餐廳（Flask 應用程式）
app = Flask(__name__)

# 步驟3：訓練服務生（定義路由）
@app.route('/')
def hello():
    return " <h1> hello world ! </h1> "

@app.route('/hello')
def customer():
    return " <h1>登入頁面</h1>"


# 步驟4：開店營業（啟動伺服器）
if __name__ == '__main__':
    app.run(debug=True)