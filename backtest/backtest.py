import backtrader as bt
import pandas as pd


class MovingAverageStrategy(bt.Strategy):
    params = (('short_period', 12), ('long_period', 26), ('stake', 0.2))

    def __init__(self):
        self.short_ma = bt.ind.SMA(self.data.close, period=self.params.short_period)
        self.long_ma = bt.ind.SMA(self.data.close, period=self.params.long_period)

    def next(self):
        if not self.position:  # 没有持仓
            if self.short_ma[0] > self.long_ma[0]:  # 12日均线穿越26日均线
                self.buy(size=self.broker.getcash() * self.params.stake / self.data.close[0])
        else:  # 持仓中
            if self.data.close[0] < self.long_ma[0]:  # 收盘价跌破26日均线
                self.sell(size=self.position.size)

def run_backtest():
    data = bt.feeds.GenericCSVData(
        dataname='./data/pingan_data.csv',  # 数据文件路径
        dtformat='%Y-%m-%d',  # 日期格式
        timeframe=bt.TimeFrame.Days,  # 时间间隔为天
        compression=1,
        openinterest=-1,  # 忽略持仓数据
        nullvalue=0.0,  # 空值填充为 0.0
        headers=True,  # 数据包含表头
        fromdate=pd.Timestamp('2023-01-01'),  # 设置起始日期
        todate=pd.Timestamp('2023-12-31')  # 设置结束日期
    )

    cerebro = bt.Cerebro()
    cerebro.adddata(data)
    cerebro.addstrategy(MovingAverageStrategy)
    cerebro.broker.setcash(1000000)
    cerebro.broker.setcommission(commission=0.0001)

    print("初始资金: %.2f" % cerebro.broker.getvalue())
    cerebro.run()
    print("最终资金: %.2f" % cerebro.broker.getvalue())
    cerebro.plot()

if __name__ == "__main__":
    run_backtest()
