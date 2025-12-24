# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# 首頁：顯示表單
@app.route('/')
def home():
    return render_template('form.html')

# 處理表單提交
@app.route('/submit', methods=['POST'])
def submit_form():
    # 從表單取得資料
    username = request.form['username']
    favorite_color = request.form.get('color', 'blue')
    message = request.form['message']
    
    # 處理資料（這裡可以做更多事情）
    word_count = len(message.split())
    
    # 準備回傳資料
    result = {
        'username': username,
        'color': favorite_color,
        'message': message,
        'word_count': word_count
    }
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)