import requests

# 设置请求 URL
url = "http://127.0.0.1:5000/api/get_results"

# 发送 GET 请求
response = requests.get(url)

# 打印响应
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
