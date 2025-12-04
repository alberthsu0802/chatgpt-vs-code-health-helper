# app.py
from flask import Flask, render_template, request, jsonify
from models.health_model import analyze_health

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health', methods=['POST'])
def health_advice():
    # 從 POST 請求中獲取使用者的資料
    user_data = request.get_json()

    # 分析使用者的健康狀況
    result = analyze_health(user_data)

    # 返回分析結果
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
