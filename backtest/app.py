from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/set_backtest', methods=['POST'])
def set_backtest():
    data = request.json
    stock = data.get('stock')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    # 在这里可以调用数据下载函数
    return jsonify({"message": "Backtest setup complete", "stock": stock, "start_date": start_date, "end_date": end_date})

from backtest import run_backtest

@app.route('/api/get_results', methods=['GET'])
def get_results():
    # 调用 run_backtest 运行回测并获取结果
    final_value = run_backtest()  # 假设 run_backtest 返回最终权益
    return_rate = (final_value - 1000000) / 1000000
    return jsonify({
        "return_rate": return_rate,
        "final_value": final_value
    })


if __name__ == '__main__':
    app.run(debug=True)
