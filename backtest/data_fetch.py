import tushare as ts
import pandas as pd

# 设置 Tushare Token
ts.set_token("0840087578356b4c42df8b166634afa4403ea0b22206dc9c87378e50")  # 替换为你的实际 Token
pro = ts.pro_api()

# 获取平安银行股票数据
def fetch_data():
    df = pro.daily(ts_code='000001.SZ', start_date='20230101', end_date='20231231')
    df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
    df = df.sort_values('trade_date')
    df = df[['trade_date', 'open', 'high', 'low', 'close', 'vol']]  # 提取需要的列
    df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']  # 重命名列
    df.set_index('datetime', inplace=True)  # 设置 datetime 为索引
    df.to_csv('./data/pingan_data.csv')  # 保存为 CSV 文件
    print("数据已保存至 ./data/pingan_data.csv")

if __name__ == "__main__":
    fetch_data()
