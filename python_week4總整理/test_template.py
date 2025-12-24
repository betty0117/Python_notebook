from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Python 變數
    current_time = datetime.now().strftime("%H:%M:%S")
    visitor_count = 50  # 假設的訪客數
    messages = ["歡迎光臨！", "今天天氣真好", "一起學程式吧！"]

    # 傳遞到 HTML 模板
    return render_template('home.html',
                         time=current_time,
                         count=visitor_count,
                         messages=messages)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)