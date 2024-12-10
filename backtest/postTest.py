import requests

# 设置请求 URL 和数据
url = "http://127.0.0.1:5000/api/set_backtest"
data = {
    "stock": "000001.SZ",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 打印响应
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
