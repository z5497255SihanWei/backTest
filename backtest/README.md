# **API 使用方法**

本项目提供了两个 API，分别用于设置回测参数和获取回测结果。以下是详细的使用说明。

---

## **1. 设置回测 (POST `/api/set_backtest`)**

### **功能**
设置回测的股票代码、起始日期和结束日期。

### **请求示例**
```
{
    "stock": "000001.SZ",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}
```
响应示例
```
{
    "message": "Backtest setup complete",
    "stock": "000001.SZ",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}
```
## **2. 获取回测结果 (GET /api/get_results)**
用于获取回测的收益率和最终权益。

响应示例
```
{
    "return_rate": 0.15,
    "final_value": 1150000
}
```
## **运行说明**
启动 Flask 服务：

在终端中运行以下命令：
```
python app.py
```
服务启动后，访问地址为 http://127.0.0.1:5000。
测试 API：

可以使用 postTest.py 和 getTest.py 脚本测试 API，或使用工具如 Postman 进行请求。